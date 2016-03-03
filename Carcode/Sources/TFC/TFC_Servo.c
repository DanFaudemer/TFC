#include "TFC\TFC.h"
#include "constants.h"

#define FTM1_CLOCK           (CORE_CLOCK)
#define FTM1_CLK_PRESCALE    6// Prescale Selector value - see comments in Status Control (SC) section for more details
#define FTM1_OVERFLOW_FREQUENCY 50  // Desired Frequency of PWM Signal - Here 50Hz => 20ms period
// use these to dial in servo steering to your particular servo
#define SERVO_MIN_DUTY_CYCLE   750 // ->  5% DC (1ms)    //(float)(.0010*FTM1_OVERFLOW_FREQUENCY)  // The number here should be be *pulse width* in seconds to move servo to its left limit
#define SERVO_MAX_DUTY_CYCLE   1500// -> 10% DC (2ms)    //(float)(.0020*FTM1_OVERFLOW_FREQUENCY)  // The number here should be be *pulse width* in seconds to move servo to its Right limit
/**********************************************************************************************/


int16_t offsetServo = 200;
//Position is -1000 to 1000 : pos in % *1000 (ex: 0.5*1000=500 -> 50% * 90°).  //  Use SERVO_X_MIN_DUTY_CYCLE and SERVO_MAX_DUTY_CYCLE  to calibrate the extremes
//          => -90° to 90°
void TFC_SetServo(uint8_t ServoNumber, int16_t Position)
{
    uint16_t DutyCycle=0;
    Position += offsetServo; //Correct the offset of the servo 
    
	/* application Range limitation for the Servo */
	if (Position < SERVOMIN)
		Position = SERVOMIN;
	else if (Position> SERVOMAX)
		Position = SERVOMAX;
    
    //
    // Counter Period: 20ms -> N=15000 (freq 750kHz)
    // servo min     :pulse width: 1ms  -> 5%  DC -> N=750 : SERVO_MIN_DUTY_CYCLE
    // servo center  :pulse width: 1.5ms-> 7.5%DC -> N=1125
    // servo max     :pulse width: 2ms  -> 10% DC -> N=1500 : SERVO_MAX_DUTY_CYCLE
    
    DutyCycle = (Position+1000)*(SERVO_MAX_DUTY_CYCLE-SERVO_MIN_DUTY_CYCLE)/2000+SERVO_MIN_DUTY_CYCLE;
	TFC_SetServoDutyCycle(ServoNumber , DutyCycle );

}

void TFC_SetServoDutyCycle(uint8_t ServoNumber, uint16_t DutyCycle) // DutyCycle : percent(int 16) *100
{
	switch(ServoNumber)
	{
	default:
	case 0:
		TPM1_C0V = DutyCycle;    //[0-15000], 15000<->20ms        // defaut: [(TPM1_MOD * DutyCycle); ]
		break;

	case 1:
		TPM1_C1V = DutyCycle;          //defaut:[(TPM1_MOD * DutyCycle); ]
		break;
	}
}

/******************************************* Function to control Interrupt ************************************/
volatile unsigned char ServoTickVar;

void FTM1_IRQHandler()
{
	//Clear the overflow mask if set.   According to the reference manual, we clear by writing a logic one!
	if(TPM1_SC & TPM_SC_TOF_MASK)
		TPM1_SC |= TPM_SC_TOF_MASK;

	if (ServoTickVar < 0xff)//if servo tick less than 255 count up... 
		ServoTickVar++;

}

void TFC_InitServos()
{

	//Clock Setup for the TPM requires a couple steps.



	//1st,  set the clock mux
	//See Page 124 of f the KL25 Sub-Family Reference Manual, Rev. 3, September 2012
	SIM_SOPT2 |= SIM_SOPT2_PLLFLLSEL_MASK;// We Want MCGPLLCLK/2 (See Page 196 of the KL25 Sub-Family Reference Manual, Rev. 3, September 2012) : 24MHz
	SIM_SOPT2 &= ~(SIM_SOPT2_TPMSRC_MASK);
	SIM_SOPT2 |= SIM_SOPT2_TPMSRC(1); //We want the MCGPLLCLK/2 (See Page 196 of the KL25 Sub-Family Reference Manual, Rev. 3, September 2012)


	//Enable the Clock to the FTM0 Module
	//See Page 207 of f the KL25 Sub-Family Reference Manual, Rev. 3, September 2012
	SIM_SCGC6 |= SIM_SCGC6_TPM1_MASK; 

	//The TPM Module has Clock.  Now set up the peripheral

	//Blow away the control registers to ensure that the counter is not running
	TPM1_SC = 0;
	TPM1_CONF = 0;

	//While the counter is disabled we can setup the prescaler
	TPM1_SC = TPM_SC_PS(5);//presc=32 -> clock TPM1: 750kHz                   defaut:[FTM1_CLK_PRESCALE); //prescaler 64 : clock: 350kHz (clk TMP1:24MHz)]
	TPM1_SC |= TPM_SC_TOIE_MASK; //Enable Interrupts for the Timer Overflow

	//Setup the mod register to get the correct PWM Period
	
	//DAN : Change to 10000 that seems working for this servo. So the period is < 20ms   
	TPM1_MOD =10000;// 15000 ; // freq servo = 50Hz -> P=20ms * 750kHz -> 15000    // defaut: [FTM1_CLOCK/(1<<(FTM1_CLK_PRESCALE+1))/FTM1_OVERFLOW_FREQUENCY; //48M/(128*50)=7500  -> at 350kHz => period = 21.4ms]

	//Setup Channels 0 and 1 as PWM (counter up, output clear on match, set on reload)
	TPM1_C0SC = TPM_CnSC_MSB_MASK | TPM_CnSC_ELSB_MASK;
	TPM1_C1SC = TPM_CnSC_MSB_MASK | TPM_CnSC_ELSB_MASK;

	//Enable the Counter

	//Set the Default duty cycle to servo neutral
	TFC_SetServo(0, 0);
	TFC_SetServo(1, 0);

	//Enable the TPM COunter
	TPM1_SC |= TPM_SC_CMOD(1);

	//Enable TPM1 IRQ on the NVIC
	enable_irq (INT_TPM1-16);

	//Enable the FTM functions on the the port

	PORTB_PCR0 = PORT_PCR_MUX(3);
	PORTB_PCR1 = PORT_PCR_MUX(3);

}

