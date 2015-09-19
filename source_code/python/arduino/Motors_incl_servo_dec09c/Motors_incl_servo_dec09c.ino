#include <Servo.h>

/*
 * Robot Motor Controller script with PWM speed control
 */
//---------------------- Motors
// This Sketch uses the H-bridge Chip from pololu and
//  incorperates the use of a servo motor attached to
//   Digital Pin 12.
//
// All Arduino Sketches are completed by Cian Byrne as 
//  part of the CMDrobots project in 2012 / 2013.
//
//

Servo myservo; //creates a servo object
int motorLHigh = 4;
int motorLLow = 2;
int motorLPWM = 5;
int motorRHigh = 7;
int motorRLow = 8;
int motorRPWM = 6;
int ledPin = 13;
int Byte1 = 0;  //for incoming serial data
int Byte2 = 0;  //for incoming serial data
int Byte3 = 0;  //for incoming serial data
int Byte4 = 0;  //for incoming serial data
int motor_a = 0;
int motor_b = 0;
int dir_y = 0;
int servo = 90; //for servo position, 90* is middle, 0* is extreme left (for turning), 180* is extreme right (when turning).


void setup() {
Serial.begin(9600);  // opens serial port, sets data rate at 9600bps
myservo.attach(9); // attaches servo to pin 12
pinMode(motorLPWM, OUTPUT);
pinMode(motorRPWM, OUTPUT);
pinMode(motorRHigh, OUTPUT);
pinMode(motorRLow, OUTPUT);
pinMode(motorLHigh, OUTPUT);
pinMode(motorLLow, OUTPUT);
pinMode(ledPin, OUTPUT);
}


void loop() {
digitalWrite(ledPin, HIGH);

if(Serial.available() > 0)
{
  Byte1 = Serial.read(); // Incoming data from Serial connection Byte 1
  motor_a = int(Byte1);
  Byte2 = Serial.read(); // Incoming data from Serial connection Byte 2
  motor_b = int(Byte2);
  Byte3 = Serial.read(); // Incoming data from Serial connection Byte 3
  dir_y = int(Byte3);
  Byte4 = Serial.read(); // Incoming data from Serial connection Byte 4 for Servo
  servo = int(Byte4);
  
  if (dir_y == 2) { //Motor Backwards
  digitalWrite(motorLLow, HIGH);
  digitalWrite(motorLHigh, LOW);
  digitalWrite(motorRLow, HIGH);
  digitalWrite(motorRHigh, LOW);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  myservo.write(servo);
  }
  else if (dir_y == 1) {  //Motor Forwards and Single motor Turning
  digitalWrite(motorLLow, LOW);
  digitalWrite(motorLHigh, HIGH);
  digitalWrite(motorRLow, LOW);
  digitalWrite(motorRHigh, HIGH);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  myservo.write(servo);
  }
  }
  
}

