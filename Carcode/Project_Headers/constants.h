/*
 * constants.h
 *
 *  Created on: May 1, 2014
 *      Author: Dan
 */

#ifndef CONSTANTS_H_
#define CONSTANTS_H_

#define LIMITCAMMIN 20
#define LIMITCAMMAX 115
#define LINECENTER 70
#define LINE_SIZE 85 

#define SEUIL_DETECTION_1 (seuil_detection/4)
#define SEUIL_DETECTION_2 (seuil_detection/2)
#define SEUIL_DETECTION_3 (seuil_detection-seuil_detection/4)
#define SEUIL_DETECTION_4 (seuil_detection)

#define SERVOMIN -500 // -34.0% * 90°
#define SERVOMAX 1200 // 80.0% * 90°


//#define abs(a) ((a<0) ? (-a) : (a))


/* States machine */
#define DEBUG 0
#define RUN 1


#endif /* CONSTANTS_H_ */
