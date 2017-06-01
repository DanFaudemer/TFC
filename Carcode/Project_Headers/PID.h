/*
 * PID.h
 *
 *  Created on: Jul 4, 2014
 *      Author: B48861
 */

#ifndef PID_H_
#define PID_H_


/* PID Coefficient */
int16_t coeff_dir_P = 900; //coeff *1000
int16_t coeff_dir_D = 370;
int16_t coeff_dir_I =	0;


int16_t coeff_diff_P =0;
int16_t coeff_diff_I =0;
int16_t coeff_diff_D =0;

int16_t coeff_speed_P =200;
int16_t coeff_speed_I =0;
int16_t coeff_speed_D =0;


int16_t differentiel_max=300;
int16_t vit_max = 600;
int16_t vit_min = 450;
uint8_t  break_min_error = 0;

int16_t deadBand = 0;
#endif /* PID_H_ */
