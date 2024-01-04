/****************************************************
*Credits to Enjoy Mechatronics for the original code:
*https://www.youtube.com/watch?v=880UQUgUD2M
*
*Son Nam Nguyen
*WPI - BME2210
*Humidity & Temperature Sensor
****************************************************/

#include "dht.h"
#include "LiquidCrystal_I2C.h"
#define dht_apin A0 //Define DHT11 pin                               
#define BUZZER_PIN 8 //Define passive sound buzzer pin  

dht DHT;
int humidity;
int temperature;

LiquidCrystal_I2C lcd(0x27, 16, 2); //Declare the settings for LCD

const int threshold = 10; //Declare the temperature threshold
 
void setup(){

  lcd.init(); //Inititiate LCD
  lcd.backlight(); 

  pinMode(BUZZER_PIN, OUTPUT); //Set buzzer pin to output
  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
}

void loop(){
  
  delay(1000); //Delay system to wait for DHT11 to start measurement
    
  DHT.read11(dht_apin); //DHT starts the measurement  
  humidity = DHT.humidity;
  temperature = DHT.temperature;
    
  lcd.setCursor(3,0); //Set the first line to print on the LCD
  lcd.print("Humidity: ");
  lcd.print(humidity);
  lcd.print("%  ");

  lcd.setCursor(0,1); //Set the first line to print on the LCD
  lcd.print("Temperature: ");
  lcd.print(temperature);
  lcd.print("C  ");

  if (temperature < threshold) {  // if humidity exceeds a threshold
    tone(BUZZER_PIN, 420);      // then play a 420 Hz tone
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
  } else {                 
    noTone(BUZZER_PIN);         // turn off the buzzer
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
  }
}
