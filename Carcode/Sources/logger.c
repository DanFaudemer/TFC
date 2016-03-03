/*
 * logger.c
 *
 *  Created on: Jul 28, 2014
 *      Author: B48861
 */

#include "logger.h"

#define WAIT_TIME 30000 //Slow speed for python script & buffer 

uint8_t log_full = 0; 

dataLog saveData[LOG_SIZE];

unsigned int posLog =0;
void logger(dataLog data)
{

	// To continue... 

	saveData[posLog] = data;
	posLog++;
	if(posLog >= LOG_SIZE)
	{
		posLog = 0;
		log_full = 1;
	}

	return ;
}

void printLastLog()
{
	unsigned int lastDataPos = posLog - 1;
	TERMINAL_PRINTF("Line Pos : %d\r\n", saveData[lastDataPos].linePos);
	TERMINAL_PRINTF("Ticker : %d\r\n", saveData[lastDataPos].ticker);
	TERMINAL_PRINTF("VitesseG : %d\r\n", saveData[lastDataPos].vitesseG);
	TERMINAL_PRINTF("VitesseD : %d\r\n", saveData[lastDataPos].vitesseD);
	TERMINAL_PRINTF("Direction pos : %d\r\n", saveData[lastDataPos].pos);
	TERMINAL_PRINTF("Pos in log buffer : %d\r\n", lastDataPos);
}
void printLogger()
{
	unsigned int start=0, i, temp, junk;
	unsigned int end = LOG_SIZE;
	if(log_full)
		start = posLog+1;
	else
		end = posLog+1;
	TERMINAL_PRINTF("BEGIN_LOG\r\n");
	TERMINAL_PRINTF("Line Pos : \r\n");
	
	for(i=start; i < end; i++)
	{
		TERMINAL_PRINTF("%d\r\n", saveData[i].linePos);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
			
		}
		
	}
	for(i=0; i < start; i++)
	{
		TERMINAL_PRINTF("%d\r\n", saveData[i].linePos);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}

	TERMINAL_PRINTF("Ticker : \r\n");
	for(i=start; i < end; i++)
	{
		TERMINAL_PRINTF("%d\r\n", saveData[i].ticker);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}
	for(i=0; i < start; i++)
	{
		TERMINAL_PRINTF("%d\r\n", saveData[i].ticker);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}


	TERMINAL_PRINTF("VitesseG : \r\n");
	for(i=start; i < end; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].vitesseG);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}
	for(i=0; i < start; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].vitesseG);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}

	TERMINAL_PRINTF("VitesseD : \r\n");
	for(i=start; i < end; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].vitesseD);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}
	for(i=0; i < start; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].vitesseD);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}

	TERMINAL_PRINTF("Direction pos : \r\n");
	TFC_UART_Process();
	for(i=start; i < end; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].pos);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}
	for(i=0; i < start; i++){
		TERMINAL_PRINTF("%d\r\n", saveData[i].pos);
		TFC_UART_Process();
		for(temp = 0;temp<WAIT_TIME;temp++)
		{
		}
	}
	
	TERMINAL_PRINTF("END_LOG\r\n");
	TFC_UART_Process();

}
