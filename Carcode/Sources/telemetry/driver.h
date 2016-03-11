/*
 * driver.h
 *
 *  Created on: Mar 4, 2016
 *      Author: B48861
 */

#ifndef DRIVER_H_
#define DRIVER_H_

#include "telemetry_utils.h"

int32_t write(void * buf, uint32_t sizeToWrite);
int32_t writeable();
int32_t read(void * buf, uint32_t sizeToRead);
int32_t readable();
void getTelem(TM_state * state,  TM_msg * msg);
void publish_vars();





#endif /* DRIVER_H_ */
