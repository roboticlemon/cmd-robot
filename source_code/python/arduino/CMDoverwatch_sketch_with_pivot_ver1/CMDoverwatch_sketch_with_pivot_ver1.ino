/*
 * Robot Motor Controller script with PWM speed control
 */
//---------------------- Motors
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
int motor_a = 0;
int motor_b = 0;
int dir_y = 0;


void setup() {
Serial.begin(9600);  // opens serial port, sets data rate at 9600bps
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

if(Serial.available()==3)
{
  Byte1 = Serial.read(); // Incoming data from Serial connection
  motor_a = int(Byte1);
  Byte2 = Serial.read(); // Incoming data from Serial connection
  motor_b = int(Byte2);
  Byte3 = Serial.read(); // Incoming data from Serial connection
  dir_y = int(Byte3);
  
  if (dir_y == 1) {  //Motor Forwards and Single motor Turning
  digitalWrite(motorLLow, LOW);
  digitalWrite(motorLHigh, HIGH);
  digitalWrite(motorRLow, LOW);
  digitalWrite(motorRHigh, HIGH);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }
  else if (dir_y == 2) { //Motor Backwards
  digitalWrite(motorLLow, HIGH);
  digitalWrite(motorLHigh, LOW);
  digitalWrite(motorRLow, HIGH);
  digitalWrite(motorRHigh, LOW);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);

  }
  else if (dir_y == 3) {  //Pivot Right
  digitalWrite(motorLLow, HIGH);
  digitalWrite(motorLHigh, LOW);
  digitalWrite(motorRLow, LOW);
  digitalWrite(motorRHigh, HIGH);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }  
  else if (dir_y == 4) {  //Pivot Left
  digitalWrite(motorLLow, LOW);
  digitalWrite(motorLHigh, HIGH);
  digitalWrite(motorRLow, HIGH);
  digitalWrite(motorRHigh, LOW);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }
  }
  
}

