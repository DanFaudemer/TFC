/*
 * PID.h
 *
 *  Created on: Jul 4, 2014
 *      Author: B48861
 */

#ifndef PID_H_
#define PID_H_


/* PID Coefficient */
int16_t coeff_dir_P = 520; //coeff *1000
int16_t coeff_dir_D = 370;
int16_t coeff_dir_I =	0;


int16_t coeff_diff_P =2;
int16_t coeff_diff_I =0;
int16_t coeff_diff_D =2;

int16_t coeff_speed_P =52;
int16_t coeff_speed_I =0;
int16_t coeff_speed_D =10;


int16_t differentiel_max=300;
int16_t vit_max = 600;
int16_t vit_min = 450;
uint8_t  break_min_error = 0;

#endif /* PID_H_ */
