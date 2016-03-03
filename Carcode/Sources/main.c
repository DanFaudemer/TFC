#include "derivative.h" /* include peripheral declarations */
#include "TFC\TFC.h"
#include "constants.h"
#include "PID.h"
#include "signalProcessing.h"
#include "logger.h"

#include "./distantio.h"



/******************/

/* Function Prototypes */
void State_Debug(void);
void State_Run(void);
int16_t Asserv_pos(void);
void Asserv_vit(void);
void Update_LED(void);
/***********************/

/* Global variables and extern */
extern volatile uint16_t PotADC_Value[2];
extern uint16_t seuil_detection ;
extern uint8_t copy_nb_line;
extern uint16_t seuil_detection;
int16_t posCenter;
int16_t diff;
int16_t PWM_lights = 15000; //50% DC sur 50Hz...

int8_t cur_state=0;
int16_t vitesseG=0;
int16_t vitesseD=0;

int16_t lineError = 0;
int32_t Run_F=0;

//uint16_t  LineScanBufferCopy [128];
uint16_t  LineScanBufferCopyFiltered [128];
int16_t copyDerivate[128];
int16_t pid_speedCopy, pid_diffCopy;

uint32_t TFC_Ticker_0_copy = 0;

extern int16_t offsetServo;
/*******************************/

int main(void)
{

	//int8_t next_state=0;
	int8_t ButtonA_p = 0;
	int8_t ButtonA_isPressed = 0;
	/* Initialisation */
	
	
	
		TFC_Init();

	
    init_serial();
    init_protocol();
	init_distantio();
		
	/* Main Loop */
	
	//Read only register -> 0
	register_scalar(&Run_F, UINT8, 1, "Run_F");
	register_scalar(&vitesseG, INT16,0, "VitesseG");
	register_scalar(&vitesseD, INT16,0, "VitesseD");
    register_scalar(&pid_speedCopy, INT16,0,"PID Speed");
    register_scalar(&pid_diffCopy, INT16,0,"PID Diff");
	
	register_scalar(&posCenter, INT16,0, "Center position");
	
	register_scalar(&lineError, INT16,0, "Line error");
	
	register_scalar(&PWM_lights, INT16,1, "Lights PWM");
	register_scalar(&diff, INT16,1, "Commande servo");
	
	register_scalar(&copy_nb_line, UINT8, 0, "Nombre de lignes");
	//Line 
	register_array(LineScanImage1,128,UINT16,0,"line");
	register_array(LineScanBufferCopyFiltered,128,UINT16,0,"line filtered");
	register_array(copyDerivate,128,INT16,0,"line derivate");
	
	register_scalar(&TFC_Ticker_0_copy, UINT32, 0, "Ticker 0");
		
	register_scalar(&coeff_dir_P,INT16,1, "coeff_dir_P");
	register_scalar(&coeff_dir_D,INT16,1, "coeff_dir_D");
	register_scalar(&coeff_dir_I,INT16,1, "coeff_dir_I");
	register_scalar(&coeff_diff_P,INT16,1, "coeff_diff_P");
	register_scalar(&coeff_diff_I,INT16,1, "coeff_diff_I");
	register_scalar(&coeff_diff_D,INT16,1, "coeff_diff_D");
	register_scalar(&coeff_speed_P,INT16,1, "coeff_speed_P");
	register_scalar(&coeff_speed_I,INT16,1, "coeff_speed_I");
	register_scalar(&coeff_speed_D,INT16,1, "coeff_speed_D");
	
	register_scalar(&offsetServo, INT16,1,"offsetServo");
	
	
	register_scalar(&vit_max,INT16,1, "vit_max");
	register_scalar(&vit_min,INT16,1, "vit_min");
	register_scalar(&seuil_detection,UINT16,1, "seuil_detection");

	
	             
	for(;;)
	{	   
		//TFC_Task must be called in your main loop.  This keeps certain processing happy (I.E. Serial port queue check)
		TFC_Task();

		//TERMINAL_PRINTF("Hello \r\n");
		ButtonA_isPressed = TFC_PUSH_BUTTON_0_PRESSED;

		/* Proceed Data from UART */
		switch(cur_state)
		{
		case DEBUG: if(ButtonA_isPressed && !ButtonA_p)
		{
			TFC_Delay_mS(200);
			cur_state=RUN;
			Update_LED();
			
			if( ((TFC_GetDIP_Switch())&0x01)) // le switch 1
			{
				TFC_HBRIDGE_ENABLE;
				//Run_F=1;
			}
			else				
				TFC_HBRIDGE_DISABLE;
			
		}
		else
			State_Debug();
		break;

		case RUN: if(ButtonA_isPressed && !ButtonA_p) 
		{
			TFC_Delay_mS(200);
			cur_state=DEBUG;
            Run_F=!Run_F;
		}
		else
			State_Run();
		break;

		}

		
		ButtonA_p = ButtonA_isPressed;


	}
	return 0;
}

/***************************************************
 **                                                **
 **           State Machine  Functions             **
 **   									          **
 ****************************************************/ 
void State_Debug(void)
{
	uint32_t t,i=0;
	uint8_t j =0;
	TFC_HBRIDGE_DISABLE;
	if(TFC_Ticker[0]>1000 && LineScanImageReady==1) // Each 1s 
	{
		/* Copy line scan for logs*/
		
		
		TFC_Ticker[0] = 0;

		LineScanImageReady=0;
		//uint8_t val = TFC_ReadPot(0);
		//TERMINAL_PRINTF("New Expo Time: 0x%X \n\r", PotADC_Value[0]); //0x000 - 0xFFF
		TFC_SetLineScanExposureTime((uint32_t) (PotADC_Value[0]+100)*10); //100 to 4095+100


		posCenter = getCenterPos(LineScanImage1);

					                                       
					                                       
		diff = Asserv_pos();
		/* Set Servo Position Maximum range is 1000 */
		TFC_SetServo(0,diff);

		TERMINAL_PRINTF("Pos Serv : %d \r\n",diff);
		vitesseG = (int16_t) (TFC_ReadPot(1)*1000);
		vitesseD = vitesseG;
		if( ((TFC_GetDIP_Switch()>>1)&0x03) == 0) // les deux du milieu
		{
			TFC_HBRIDGE_ENABLE;
			TFC_SetMotorPWM(vitesseD,vitesseG); // moteur A -> droite
		}
		else
		{
			TFC_SetMotorPWM(0,0);
			TFC_HBRIDGE_DISABLE;
			TFC_SetMotorPWM(0,0);
		}
        
        /* phares PWM */
        if(TFC_GetDIP_Switch()&0x08) // if switch 4 is High
        {
            TFC_SetServoDutyCycle(1, PWM_lights); 
        }
        else 
            TFC_SetServoDutyCycle(1, 0); 

		/* Transmit Image */
		TERMINAL_PRINTF("\r\n");

		TERMINAL_PRINTF("L:,");
		for(i=0;i<128;i++)
		{
			TERMINAL_PRINTF("0x%X,",LineScanImage1[i]);
		}
		TERMINAL_PRINTF("\r\n");

		/* Transmit Position &  Parameters PID */
		TERMINAL_PRINTF(" posCenter : %d, AngleCorr : %d, diff: %d, LCenter: %d,", posCenter, diff*35, diff, (int)LINECENTER);

		/* Transmit Vitesse */
		//TERMINAL_PRINTF(" vitD: %d, vitG: %d\n\r", (int)vitesseD,(int)vitesseG);

		update_distantio();
	}
	
	Update_LED();
}


void State_Run(void)
{	
	uint8_t j =0;

	
	
	
	
	if(TFC_Ticker[0]>5 && LineScanImageReady==1) // Each 10ms 
	{
		
		//TFC_Ticker[0] = 0;
		//dataToLog.ticker = TFC_Ticker[0];
		TFC_Ticker_0_copy =  TFC_Ticker[0];
		TFC_Ticker[0] = 0;
		
		

		LineScanImageReady=0;
		//TFC_SetLineScanExposureTime((uint32_t) (PotADC_Value[0]+500)*10); //100 to 4095+100

		

		
		for( j=1; j < 128; j++)
		{
			LineScanBufferCopyFiltered[j] = (LineScanImage1[j] + LineScanImage1[j-1])>>2;
		}
		LineScanBufferCopyFiltered[0] = LineScanBufferCopyFiltered[1];
		
		
		posCenter = getCenterPos(LineScanBufferCopyFiltered);
				
		diff = Asserv_pos();

		/* Set Servo Position Maximum range is 1000 */
		TFC_SetServo(0,diff);					

		/* Set motor speed */
		Asserv_vit();
		//vitesseG = TFC_ReadPot(1);
		//vitesseD = vitesseD;
		
		if(Run_F==1)
            TFC_HBRIDGE_ENABLE;
			
		else
			TFC_HBRIDGE_DISABLE;
        TFC_SetMotorPWM(vitesseD,vitesseG); // moteur A -> droite
        
		/*
		if( ((TFC_GetDIP_Switch()>>1)&0x03) == 0)
		{
			//TFC_HBRIDGE_ENABLE;
			TFC_SetMotorPWM(vitesseD,vitesseG); // moteur A -> droite
		}
		else
			TFC_HBRIDGE_DISABLE;

        /* phares PWM */
        if(TFC_GetDIP_Switch()&0x08) // if switch 4 is High
        {
            TFC_SetServoDutyCycle(1, PWM_lights); 
        }
        else 
            TFC_SetServoDutyCycle(1, 0); 
            
		/* Transmit Position &  Parameters PID */
		//TERMINAL_PRINTF("\rposCenter : %d\n\r",posLine);



		//TERMINAL_PRINTF("\rposCenter : %d, AngleCorr : %d, diff %d, LCenter %d\n\r", posCenter, (int)(((float) diff)/35.0*1000), (int)diff, (int)LINECENTER);

        //update_distantio();

	}

	else if(TFC_Ticker[3] > 10) 
	{
		TFC_Ticker[3] = 0;
		update_distantio();
	}
}

/***************************************************
 **                                                **
 **           Other  Functions                     **
 **   									          **
 ****************************************************/ 
int16_t Asserv_pos(void)
{
	static int16_t  error =0, last_error = 0;
	int16_t  derivate=0, integrate=0;
	int16_t difference=0;


	//previous = posCenter;

	//if(posCenter == 0) // Line not found 
	//		posCenter = previous; //Wheel position has not change 

	/* Error */
	last_error = error;
	error = posCenter;

	derivate = error - last_error;
	integrate += error;
	if(integrate > 100) integrate=100;
	else if(integrate <-100) integrate=-100;

	/* PID */
	difference = (coeff_dir_P*(error) + coeff_dir_D*(derivate) + coeff_dir_I*(integrate))/35; //Derivate is bad it's on the error 
	if(difference > 1000)	difference = 1000;
	else if (difference < -1000) difference = -1000;
	// -> comment tu calcules 35? Je l'ai mesuré :D  
	// -> problème range : effective => 65 - 80 (lorsque que posline = 65 ou 80, servo à fond!)
	
	//TERMINAL_PRINTF("Difference %f, posCenter %d : \r\n", difference, posCenter);

	
	lineError = error; //Just for the log  
	
	return difference; //diff -1000 to 1000
}

void Asserv_vit(void)
{


	static int16_t  error =0, last_error = 0;
	int16_t  derivate, integrate =0;
	int16_t pid_speed, pid_diff;
	last_error = error;
	error = posCenter;

	derivate = error - last_error;
	integrate += error;	

	if(integrate > 100) integrate=100;
	else if(integrate <-100) integrate=-100;



	pid_speed = coeff_speed_P*(error) + coeff_speed_D*(derivate) + coeff_speed_I*(integrate); 
	pid_diff = coeff_diff_P*( error) + coeff_diff_D*(derivate) + coeff_diff_I*(integrate);
	
	pid_speedCopy = pid_speed;
	pid_diffCopy = pid_diff;

	vitesseG = vit_max - abs(pid_speed);
	vitesseD = vit_max - abs(pid_speed);
	
	if(vitesseG < vit_min)
		vitesseG = vit_min;
	
	if(vitesseD < vit_min)
			vitesseD = vit_min;
	//TERMINAL_PRINTF("VitesseG=%f, VitesseD=%f \r\n", vitesseG, vitesseD);		


	if(pid_diff > 0 && pid_diff > differentiel_max )
		pid_diff = differentiel_max;
	else if (pid_diff < 0 && pid_diff < differentiel_max )
		pid_diff = -differentiel_max;
	
	
	vitesseG = vitesseG - pid_diff;
	vitesseD = vitesseD + pid_diff;

	//TERMINAL_PRINTF("2 VitesseG=%f, VitesseD=%f \r\n", vitesseG, vitesseD);		

	if(vitesseG > 1000) vitesseG=1000;
	else if(vitesseG < 0) vitesseG = 0;

	if(vitesseD > 1000) vitesseD=1000;
	else if(vitesseD < 0) vitesseD = 0;
	
	/*
	
	if( abs(error) <= 2 )
	{
		vitesseG = vit_max;
		vitesseD = vit_max;
	}
	*/
	
	//Pour débug utiliser : 
	
	

	/* Jerome Proportionnel et intégrer à la commande de la direction*/
	/*
	float offset=0; 
	float differentiel=diff/(35*4), temp=0;// entre -0.25 et 0.25
	static float I_differentiel=0.0;

	I_differentiel += differentiel;

	if(I_differentiel > 10.0) I_differentiel = 10.0;
	else if (I_differentiel < -10.0) I_differentiel = -10.0;
	// vitesse moyenne en fonction du potar
/*	if( offset < VITMIN) offset = 0.3; //min
	else if(offset > 0.75) offset = 0.75; // max 0.75
	 */
	/*
	if(I_differentiel < 0) temp = I_differentiel * (-1.0) *0.1;
	else  temp = I_differentiel * 0.1;
	//vitesse moyenne en fonction de l'integrale de la position(diff) et vitesse max = potar
	offset = TFC_ReadPot(1)-temp;

	/* bornes offset */
	/*
	if(offset < VITMIN) offset = VITMIN; //0.3
	else if(offset > 0.9) offset = 0.9;

	vitesseG=offset+differentiel;
	vitesseD=offset-differentiel;

	TERMINAL_PRINTF("\rI_diff: %d\ntemp: %d\npotar: %d\noffset: %d\nvitG : %d\nvitD : %d\n\r",(int)(I_differentiel*1000.0),
			(int) (temp*1000.0), (int)(TFC_ReadPot(1)*1000.0), (int)(offset*1000.0), (int)(vitesseG*1000.0), (int)(vitesseD*1000.0));

	if(vitesseG > 1.0) vitesseG=1.0;
	else if(vitesseG < 0.0) vitesseG = 0.0;

	if(vitesseD > 1.0) vitesseD=1.0;
	else if(vitesseD < 0.0) vitesseD = 0.0;*/

}


void Update_LED(void)
{
	//extern int16_t min_d2;
	extern int16_t max_d2;
	float Vbat=0;
	/* Update Min the Led battery (Signal Quality ) */
	//minmaxcam(derivate2, &min_cam, &max_cam);
	//TERMINAL_PRINTF("Max value : %d \n\r", max_cam);

	if(TFC_PUSH_BUTTON_1_PRESSED) /* battery voltage  */
	{
		Vbat = TFC_ReadBatteryVoltage();
		if(Vbat <= 1.1) TFC_SetBatteryLED_Level(0);
		else if(Vbat <= 1.17 ) TFC_SetBatteryLED_Level(1);
		else if(Vbat <= 1.27 ) TFC_SetBatteryLED_Level(2);
		else if(Vbat <= 1.42 ) TFC_SetBatteryLED_Level(3);
		else TFC_SetBatteryLED_Level(4);
	}
	else
		switch(cur_state)
		{
		case DEBUG: /*  Quality of the signal  */
			if(max_d2 > SEUIL_DETECTION_4)
			{
				TFC_BAT_LED0_ON;
				TFC_BAT_LED1_ON;
				TFC_BAT_LED2_ON;
				TFC_BAT_LED3_ON;
				//TFC_BAT_LED(0x0F);

			}
			else if (max_d2 >= SEUIL_DETECTION_3)
			{
				TFC_BAT_LED0_ON;
				TFC_BAT_LED1_ON;
				TFC_BAT_LED2_ON;
				TFC_BAT_LED3_OFF;

				//TFC_BAT_LED(0x07);
			}				
			else if (max_d2 >= SEUIL_DETECTION_2)
			{
				TFC_BAT_LED0_ON;
				TFC_BAT_LED1_ON;
				TFC_BAT_LED2_OFF;
				TFC_BAT_LED3_OFF;	
				//TFC_BAT_LED(0x03);

			}

			else if (max_d2 >= SEUIL_DETECTION_1)
			{
				TFC_BAT_LED0_ON;
				TFC_BAT_LED1_OFF;
				TFC_BAT_LED2_OFF;
				TFC_BAT_LED3_OFF;
				//TFC_BAT_LED(0x01);
			}
			else
			{
				TFC_BAT_LED0_OFF;
				TFC_BAT_LED1_OFF;
				TFC_BAT_LED2_OFF;
				TFC_BAT_LED3_OFF;
				//TFC_BAT_LED(0x00);
			}
			break;

		case RUN: /* code 1 */
			TFC_SetBatteryLED_Level(1);
			break;

		default: TFC_SetBatteryLED_Level(0);
		}

}
