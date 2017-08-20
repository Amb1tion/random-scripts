#include <SoftwareSerial.h>
int inputpin = 13;
int pirState = LOW;
int val = 0;
SoftwareSerial mySerial(7,8);
void setup()
{
  mySerial.begin(9600);
  Serial.begin(9600);
  delay(100);

}
 
void loop()
{
  val = digitalRead(inputpin);
  if(val == HIGH)
  {
    mySerial.println("ATD+XXXXXXXXXXX;");
    delay(10000);
    mySerial.println("ATH");
  }
  
 
}

