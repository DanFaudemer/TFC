#include "TFC\TFC.h"
#include "constants.h"

extern int8_t cur_state;
void TFC_Init()
{
	TFC_InitClock();
	TFC_InitSysTick();
	TFC_InitGPIO();
	TFC_InitServos();
	TFC_InitMotorPWM();
    TFC_InitADCs();
    TFC_InitLineScanCamera();
    TFC_InitTerminal();
	TFC_InitUARTs();
	TFC_HBRIDGE_DISABLE;
	TFC_SetMotorPWM(0,0);
	
}

void TFC_Task()
{
	#if defined(TERMINAL_USE_SDA_SERIAL)
		TFC_UART_Process();
	#endif
	 
}
