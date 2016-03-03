#include <SoftwareSerial.h>

SoftwareSerial mySerial(8, 9); // RX, TX

void setup() {

Serial.begin(9600);

pinMode(12,OUTPUT); digitalWrite(12,HIGH);

Serial.println("Enter AT commands:");

mySerial.begin(9600);

}

void loop()

{

if (mySerial.available())

Serial.write(mySerial.read());

if (Serial.available())

mySerial.write(Serial.read());

}
