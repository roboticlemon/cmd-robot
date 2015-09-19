#include <Servo.h>

Servo myservo; //Creates a servo object

int pos = 90; //variable to store servo position
int incomingbyte;

void setup()
{
  myservo.attach(9); // attaches the servo on pin 9 to servo object
  myservo.write(90);
  Serial.begin(9600);
}

void loop()
{
if(Serial.available() > 0) {
 // read the incoming byte:
  incomingbyte = Serial.read();
  myservo.write(incomingbyte);
}
}


