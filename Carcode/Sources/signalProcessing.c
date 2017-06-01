#include "derivative.h" /* include peripheral declarations */
#include "TFC\TFC.h"
#include "constants.h"
#include "signalProcessing.h"

#include <cstdlib> 
#define MEDIAN_SIZE 1
extern int8_t cur_state;
uint16_t seuil_detection=10;
int16_t min_d2 =0, max_d2 =0;
uint8_t copy_nb_line=0;

uint16_t *copymedianFilter;
uint16_t *copygainCorr;
int16_t *copyderivate_cam;

uint16_t medianFilter_out[128], gainCorr_out[128];

int16_t derivate_out[128];
int compare( const void* a, const void* b)
{
	uint16_t int_a = * ( (uint16_t*) a );
	uint16_t int_b = * ( (uint16_t*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}

void  medianFilter(uint16_t *camera, uint16_t *out)
{
	uint16_t sub[MEDIAN_SIZE*2] = {0};
	uint8_t i,j, left, right;
	
	for(i = 0; i < 128; i++)
	{
		left  = (i-MEDIAN_SIZE > 0) ? (i-MEDIAN_SIZE) : 0;
		right = (i+MEDIAN_SIZE < 128) ? (i+MEDIAN_SIZE) : 127;
		
		for(j=left; j < right ; j++)
			sub[j-left] = camera[j];
		
		j++;
		qsort(sub, right-left, sizeof(uint16_t), compare);
		out[i] = sub[(right-left)>>1];		
	}
}

void  gainCorr(uint16_t *camera, uint16_t *out)
{
	uint16_t min, max;
	uint8_t i;
	float corr ;
	
	/*Get min max */
	min = camera[0];
	max = camera[1];
	for(i=1; i < 128 ; i ++)
	{
		if(camera[i] > max)
			max = camera[i];
		if(camera[i] < min)
			min = camera[i];
	}
	
	corr = ((float) ((1<<10)-1))/((float) max);
	for(i=0; i < 128 ; i++)
	{
		out[i] = (uint16_t)(corr*((float) camera[i]));
	}
}


void  derivate_cam(uint16_t *camera, int16_t *out)
{
	uint8_t i;
	for(i=0; i < 128-1 ; i++)
	{
		out[i] = ((int16_t) (camera[i+1]) - (int16_t) (camera[i]))/2;
	}
	
}



int16_t getPos(int16_t *camera)
{
	uint8_t i;
	int16_t i_max = -1;
	int16_t max = 0;
	for(i=LIMITCAMMIN; i < LIMITCAMMAX ; i++)
	{
		if(abs(camera[i]) > abs(max) &&  abs(camera[i]) > seuil_detection)
		{
			max = camera[i];
			i_max = i;
		}
	}
	
	if(i_max > -1)
	{
		return ((i_max <= 64) ? i_max + LINE_SIZE/2 : i_max - LINE_SIZE/2) - 64;
	}
	else
		return -1;
}

int16_t getCenterPos( uint16_t  *LineScanImage)
{
	int16_t posLine, posLine_prev;	

	
	medianFilter(LineScanImage, medianFilter_out);
	copymedianFilter = medianFilter_out,
	gainCorr(medianFilter_out, gainCorr_out);
	copygainCorr = gainCorr_out;
	derivate_cam(gainCorr_out, derivate_out);
	copyderivate_cam = derivate_out;
	posLine = getPos(derivate_out);
		
	
	return posLine;
	
}
	

void minmaxcam (int16_t  *table ,int16_t  *min ,int16_t  *max)
{
	unsigned char i;
	*min = table[0]; *max = table[0];
	
	for(i=1; i <128; i++)
	{
		if(table[i] < *min)
			*min = table[i];
		if(table[i] > *max)
			*max = table[i];
	}
	
}
