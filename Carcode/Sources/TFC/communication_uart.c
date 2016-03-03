#include "stdlib.h"

#include "TFC\TFC.h"
#include "logger.h"
#define  UART_COMMAND_MAX_SIZE 256
#define NUM_TERMINAL_COMMANDS 21
char command_buffer[UART_COMMAND_MAX_SIZE] = { };
uint8_t pos_command_buffer = 0;
const char cancel_char[] = {' ', '\n', '\r', '\t', '\0'};





extern float coeff_dir_P;
extern float coeff_dir_D;
extern float coeff_dir_I;


extern float coeff_diff_P ;
extern float coeff_diff_I ;
extern float coeff_diff_D ;

extern float coeff_speed_P ;
extern float coeff_speed_I ;
extern float coeff_speed_D ;


extern float differentiel_max;
extern float vit_max ;
extern float vit_min;
extern uint8_t  break_min_error ;

extern uint16_t seuil_detection;



typedef void (*TerminalCallback)(char *);

typedef struct {
	const char *CommandString;
	TerminalCallback Callback;
	const char * HelpString;

} CommandRecord;
void cmd_DIR_P(char *arg);
void cmd_DIR_I(char *arg);
void cmd_DIR_D(char *arg) ;
void cmd_DIFF_P(char *arg) ;
void cmd_DIFF_I(char *arg) ;
void cmd_DIFF_D(char *arg) ;
void cmd_DIFF_MAX(char *arg) ;
void cmd_SPE_P(char *arg) ;
void cmd_SPE_I(char *arg) ;
void cmd_SPE_D(char *arg) ;
void cmd_CAM_EXPO(char *arg) ;
void cmd_CAM_SEUIL(char *arg);
void cmd_Vbat(char *arg) ;
void cmd_Pos(char *arg) ;
void cmd_Pservo(char *arg) ;
void cmd_Refresh(char *arg) ;
void cmd_Help(char *arg)  ;


void cmd_SPE_MIN(char *arg);
void cmd_SPE_MAX(char *arg);
void cmd_SPE_ERROR(char *arg);

void cmd_GET_LOG(char *arg);
void cmd_GET_LAST_LOG(char *arg);
const CommandRecord MyTerminalRecords[] = { { "help", cmd_Help,"Lists available commands" },
		{ "DIR_P", cmd_DIR_P, "" },
		{ "DIR_I",cmd_DIR_I, "" }, 
		{ "DIR_D", cmd_DIR_D, "" },
		{ "DIFF_P", cmd_DIFF_P, "" },
		{ "DIFF_I", cmd_DIFF_I, "" }, 
		{ "DIFF_D",	cmd_DIFF_D, "" },
		{ "DIFF_MAX", cmd_DIFF_MAX, "" },
		{ "SPE_P",cmd_SPE_P, "" }, 
		{ "SPE_D", cmd_SPE_D, "" }, 
		{ "SPE_I",cmd_SPE_I, "" }, 
		{ "SPE_MAX",cmd_SPE_MAX, "" }, 
		{ "SPE_MIN",cmd_SPE_MIN, "" }, 
		{ "SPE_ERROR",cmd_SPE_ERROR, "Erreur minimum pour déclancher le PID du freinage, sinon vit=vit_max" }, 
		{ "CAM_EXPO", cmd_CAM_EXPO, "" },
		{ "CAM_SEUIL", cmd_CAM_SEUIL, "Seuil de détection de la caméra (default = 200)" },
		{ "Refresh",cmd_Refresh, "" },
		{ "Vbat", cmd_Vbat, "" },
		{ "Pos", cmd_Pos,"" },
		{ "GET_LOG", cmd_GET_LOG,"Get logged data" },
		{ "GET_LAST_LOG", cmd_GET_LAST_LOG,"Get logged data" },
		{ "Pservo", cmd_Pservo, "" }
		
};

void cmd_DIR_P(char *arg) {
	coeff_dir_P = (float)atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIR_P is %f \r\n",  (coeff_dir_P));
}

void cmd_DIR_I(char *arg) {
	coeff_dir_I = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIR_I is %f \r\n", coeff_dir_I);
}

void cmd_DIR_D(char *arg) {
	coeff_dir_D = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIR_D is %f \r\n",  (coeff_dir_D));
}
//////////////////////////////////////////////////////////////////////////
void cmd_DIFF_P(char *arg) {
	coeff_diff_P = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIFF_P is %f \r\n",  (coeff_diff_P));
}
void cmd_DIFF_I(char *arg) {
	coeff_diff_I = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIFF_I is %f \r\n",  (coeff_diff_I));
}

void cmd_DIFF_D(char *arg) {
	coeff_diff_D = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient DIFF_D is %f \r\n",  (coeff_diff_D));
}

void cmd_DIFF_MAX(char *arg) {
	differentiel_max = atof(arg);
	TERMINAL_PRINTF("\r\n New value for DIFF_MAX is %f \r\n", differentiel_max);
}
////////////////////////////////////////////////////////////////////// 
void cmd_SPE_P(char *arg) {
	coeff_speed_P = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient SPE_P is %f \r\n",  (coeff_speed_P));
}

void cmd_SPE_I(char *arg) {
	coeff_speed_I = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient SPE_I is %f \r\n",  (coeff_speed_I));
}

void cmd_SPE_D(char *arg) {
	coeff_speed_D = atof(arg);
	TERMINAL_PRINTF("\r\n New coefficient SPE_D is %f \r\n",  (coeff_speed_D));
}


void cmd_SPE_MAX(char *arg) {
	vit_max = atof(arg);
	TERMINAL_PRINTF("\r\n New value for SPE_MAX is %f \r\n", vit_max);
}

void cmd_SPE_MIN(char *arg) {
	vit_min = atof(arg);
	TERMINAL_PRINTF("\r\n New value for SPE_MIN is %f \r\n",  vit_min);
}

void cmd_SPE_ERROR(char *arg) {
	break_min_error = atof(arg);
	//TERMINAL_PRINTF("\r\n New value for SPE_ERROR is %d \r\n",  break_min_error);
	TERMINAL_PRINTF("\r\n Not implemented \r\n",  break_min_error);
}
////////////////////////////////////////////////////////////////////// 
void cmd_CAM_EXPO(char *arg) {
	//cam_expo = atoi(arg);
	TERMINAL_PRINTF("\r\n New exposition time is not supported  \r\n", coeff_speed_D);
}

void cmd_CAM_SEUIL(char *arg) {
	seuil_detection = atoi(arg);
	TERMINAL_PRINTF("\r\n New value for CAM_SEUIL is %d \r\n",  seuil_detection);
	
}
////////////////////////////////////////////////////////////////////// 
void cmd_Vbat(char *arg) {

	TERMINAL_PRINTF("\r\n Vbatt is %f V \r\n", TFC_ReadBatteryVoltage);
}
////////////////////////////////////////////////////////////////////// 
void cmd_Pos(char *arg) {

	TERMINAL_PRINTF("\r\n Pos is not supported \r\n");
}
////////////////////////////////////////////////////////////////////// 
void cmd_Pservo(char *arg) {

	TERMINAL_PRINTF("\r\n Servo position is not supported \r\n" );
}

void cmd_GET_LOG(char *arg) {
	printLogger();	
}

void cmd_GET_LAST_LOG(char *arg) {
	printLastLog();
}

////////////////////////////////////////////////////////////////////// 
void cmd_Refresh(char *arg) {

	TERMINAL_PRINTF(
			"\r\nDIR_P:%f;\r\n"
			"DIR_I:%f;\r\n"
			"DIR_D:%f;\r\n"

			"DIFF_P:%f;\r\n"
			"DIFF_I:%f;\r\n"
			"DIFF_D:%f;\r\n"
			"DIFF_MAX:%f;\r\n"

			"SPE_P:%f;\r\n"
			"SPE_I:%f;\r\n"
			"SPE_D:%f;\r\n"
			"SPE_MAX:%f;\r\n"
			"SPE_MIN:%f;\r\n"

			"CAM_EXPO:%d;\r\n"

			,coeff_dir_P,coeff_dir_I,coeff_dir_D, 
			coeff_diff_P,coeff_diff_I,coeff_diff_D, differentiel_max,
			coeff_speed_P,coeff_speed_I,coeff_speed_D,vit_max,vit_min,

			-1.0);

}

void cmd_Help(char *arg) {
	uint8_t i;

	TERMINAL_PRINTF("\r\n\r\nCommand List:\r\n");
	TERMINAL_PRINTF("----------------------\r\n");

	for (i = 0; i < NUM_TERMINAL_COMMANDS; i++) {
		TERMINAL_PRINTF(
				"%s  ---->  %s\r\n", MyTerminalRecords[i].CommandString, MyTerminalRecords[i].HelpString);
	}

	TERMINAL_PRINTF("\r\n\r\n");
}

void uart_communication() {
	char read_c = ' ';
	char entete[10] ="", arg[10]="";
	char *pt_tab;
	uint8_t i, i_arg, j, CmdFound;
		   
	while (TERMINAL_READABLE && read_c != ';') //Empty the queue 
	{
		
		read_c = TERMINAL_GETC;
		
		if (strchr(cancel_char, read_c) != NULL )/* Cancel char  \n \r \t...*/
		{
			pos_command_buffer = 0;			
		}
		else
		{		
			command_buffer[pos_command_buffer] = read_c;
			pos_command_buffer++;
			//Print the read character 
			TERMINAL_PRINTF("%c", read_c);
		}	
	}
	
	if (read_c == ';') // We just saw a ; end of the command => Process the new command  
	{

		pt_tab = entete;
		i_arg = 0;
		for (i = 0; i < pos_command_buffer && command_buffer[i] != ';'; i++) {
			if (command_buffer[i] == ':') {
				pt_tab[i]='\0';
				pt_tab = arg;
				i_arg = i + 1;
			} else {
				pt_tab[i - i_arg] = command_buffer[i];
			}

		}
		pt_tab[i- i_arg]='\0';
		CmdFound = FALSE;
		if (command_buffer[i] == ';') {
			for (j = 0; j < NUM_TERMINAL_COMMANDS; j++) {
				//TERMINAL_PRINTF("Compare : %s with %s \r\n", entete, MyTerminalRecords[j].CommandString);
				if (strcmp(entete, MyTerminalRecords[j].CommandString) == 0) {
					if (MyTerminalRecords[j].Callback != NULL)
						MyTerminalRecords[j].Callback(arg);

					CmdFound = TRUE;
					break;
				}
			}

			if (CmdFound == FALSE) {
				TERMINAL_PRINTF("\r\n Error : Command not Found %s \n\r", entete);

			}

		} else {
			TERMINAL_PRINTF("\r\n Error : ; not found ! \n\r");
		}
		pos_command_buffer = 0;
	}

}

