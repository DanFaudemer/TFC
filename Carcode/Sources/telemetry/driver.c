/*
 * driver.c
 *
 *  Created on: Mar 4, 2016
 *      Author: B48861
 */


#include "TFC\TFC.h"

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
