#ifndef TFC_PWM_SERVO_H_
#define TFC_PWM_SERVO_H_

void TFC_InitServos();
void TFC_SetServo(uint8_t ServoNumber, int16_t Position);
void TFC_SetServoDutyCycle(uint8_t ServoNumber, uint16_t DutyCycle);

#endif /* TFC_PWM_SERVO_H_ */
