int servoPin = 9;
int Byte = 0;
int value = 0;

void setup() {
Serial.begin(9600);
pinMode(servoPin, OUTPUT);
}
void loop() {
  digitalWrite(servoPin, HIGH);
  if(Serial.available()==1) {
    Byte = Serial.read();
    value = int(Byte);
    analogWrite(servoPin, value);
  }
}
