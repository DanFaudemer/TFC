/*
 * driver.c
 *
 *  Created on: Mar 4, 2016
 *      Author: B48861
 */


#include "TFC\TFC.h"
#include "telemetry_utils.h"
#include "telemetry_core.h"

extern int16_t *copymedianFilter;
extern int16_t *copygainCorr;
extern int16_t *copyderivate_cam;
extern int16_t coeff_dir_P;
extern int16_t coeff_dir_D;
extern int16_t coeff_dir_I;
extern int16_t coeff_diff_P;
extern int16_t coeff_diff_I;
extern int16_t coeff_diff_D;
extern int16_t coeff_speed_P;
extern int16_t coeff_speed_I;
extern int16_t coeff_speed_D;
extern int16_t vit_max;
extern int16_t vit_min;
extern int16_t posCenter;
extern int16_t vitesseG;
extern int16_t vitesseD;
extern int16_t pid_speedCopy, pid_diffCopy;

extern int16_t lineError;
extern int32_t Run_F;
extern int16_t offsetServo;
extern uint32_t TFC_Ticker_0_copy;
extern int16_t diff;
extern uint16_t seuil_detection;

void publish_vars()
{
	int i;
	static int bol =0;
	char buffer[50];
	
	publish_i16("p", posCenter); 
    /*for(i=0 ; i < 127 ; i++)
    {
    	if(bol == 0)
		{
    		sprintf(buffer, "c:%d",i);
    		publish_i16(buffer,LineScanImage1[i]);
		}
    	/*
    	sprintf(buffer, "m:%d",i);
		publish_i16(buffer,copymedianFilter[i]);
    	
    	
    	
    	else if(bol ==1)
    	{
    		sprintf(buffer, "g:%d",i);
			publish_u16(buffer,copygainCorr[i]);
    	}
    	else    	    	
    	{
    		sprintf(buffer, "d:%d",i);
			publish_i16(buffer,copyderivate_cam[i]);
    	}
    	bol = (bol+1)%3;
    }
    
    /*
    publish_u8("Run_F",Run_F);
    publish_i16("vitesseG",vitesseG);
    publish_i16("vitesseD",vitesseD);
    publish_i16("pid_speedCopy",pid_speedCopy);
    publish_i16("pid_diffCopy",pid_diffCopy);
    
    publish_i16("posCenter",posCenter);
    publish_i16("lineError",lineError);
    publish_i16("ServoCommand",diff);
    publish_u32("Ticker0",TFC_Ticker_0_copy);
    
    publish_i16("coeff_dir_P",coeff_dir_P);
    publish_i16("coeff_dir_D",coeff_dir_D);
    publish_i16("coeff_dir_I",coeff_dir_I);
    
    publish_i16("coeff_diff_P",coeff_diff_P);
    publish_i16("coeff_diff_I",coeff_diff_I);
    publish_i16("coeff_diff_D",coeff_diff_D);
    
    publish_i16("coeff_speed_P",coeff_speed_P);
    publish_i16("coeff_speed_I",coeff_speed_I);
    publish_i16("coeff_speed_D",coeff_speed_D);
    
    publish_i16("offsetServo",offsetServo);
    publish_i16("vit_max",vit_max);
    publish_i16("vit_min",vit_min);
    publish_i16("seuil_detection",seuil_detection);    	    
    */
}





void getTelem(TM_state * state,  TM_msg * msg)
{
	
	update_u16(msg, "seuil_detection", &seuil_detection);
	update_i16(msg, "offsetServo", &offsetServo);
	
	update_i16(msg, "coeff_dir_P", &coeff_dir_P);
	update_i16(msg, "coeff_dir_I", &coeff_dir_I);
	update_i16(msg, "coeff_dir_D", &coeff_dir_D);
	
	update_i16(msg, "coeff_diff_P", &coeff_diff_P);
	update_i16(msg, "coeff_diff_I", &coeff_diff_I);
	update_i16(msg, "coeff_diff_D", &coeff_diff_D);
	
	update_i16(msg, "coeff_speed_P", &coeff_speed_P);
	update_i16(msg, "coeff_speed_I", &coeff_speed_I);
	update_i16(msg, "coeff_speed_D", &coeff_speed_D);
		
	update_i16(msg, "vit_max", &vit_max);
	update_i16(msg, "vit_min", &vit_min);

	
	
}


int32_t write(void * buf, uint32_t sizeToWrite)
{
  uint8_t * buffer = (uint8_t *) buf;
  uint32_t i = 0;
  for(i = 0 ; i < sizeToWrite ; i++)
  {
    ByteEnqueue(&SDA_SERIAL_OUTGOING_QUEUE, (uint8_t)(buffer[i]));
  }
  return (int32_t)sizeToWrite;
}

int32_t writeable()
{
  return BytesInQueue(&SDA_SERIAL_OUTGOING_QUEUE) < SDA_SERIAL_OUTGOING_QUEUE_SIZE ;
}

int32_t read(void * buf, uint32_t sizeToRead)
{
  uint8_t * buffer = (uint8_t *)buf;
  uint32_t avail = BytesInQueue(&SDA_SERIAL_INCOMING_QUEUE);
  
  uint32_t effectiveSizeToRead = (sizeToRead <= avail) ? sizeToRead : avail;
  uint32_t i = 0;
  for(i = 0 ; i < effectiveSizeToRead ; i ++)
  {
    buffer[i] = (uint8_t)ForcedByteDequeue(&SDA_SERIAL_INCOMING_QUEUE);
  }
  return (int32_t)effectiveSizeToRead;
}

int32_t readable()
{
  return BytesInQueue(&SDA_SERIAL_INCOMING_QUEUE);
}
