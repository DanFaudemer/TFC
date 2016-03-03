/*
 * logger.h
 *
 *  Created on: Jul 28, 2014
 *      Author: B48861
 */

#ifndef LOGGER_H_
#define LOGGER_H_
#define LOG_SIZE 0 //40 000 * 8bits * 4 Max 1995 with 256 byte in uart buffer 

 #include "TFC\TFC.h"
typedef struct dataLog {
	uint8_t ticker;
	int8_t vitesseG;
	int8_t vitesseD;
	int8_t pos;
	int8_t linePos;
} dataLog;

void logger(dataLog data);
void printLogger();
void printLastLog();

#endif /* LOGGER_H_ */
