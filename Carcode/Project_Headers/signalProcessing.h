/*
 * signalProcessing.h
 *
 *  Created on: May 18, 2014
 *      Author: Dan
 */

#ifndef SIGNALPROCESSING_H_
#define SIGNALPROCESSING_H_

void minmaxcam (int16_t  *table ,int16_t  *min ,int16_t  *max);
uint16_t getLinePos( uint16_t  *LineScanImage);
int compare( const void* a, const void* b);
void  medianFilter(uint16_t *camera, uint16_t *out);
void  gainCorr(uint16_t *camera, uint16_t *out);
void  derivate_cam(uint16_t *camera, int16_t *out);
int16_t getPos(uint16_t *camera);

#endif /* SIGNALPROCESSING_H_ */
