#include <Time.h>
#include <TimeLib.h>
#include <Servo.h>
#include "DHT.h"
#define DHTPIN 8 

DHT dht(DHTPIN, DHT11);
Servo towerprosg5010;  
time_t hora;
const int LED = 13;       
const int PIR = 12;        
long distancia;
long tiempo;
int PirState = LOW;          
int val = 0;

void setup() {
  dht.begin();
  pinMode(LED, OUTPUT); 
  pinMode(PIR, INPUT);
  pinMode(11, OUTPUT); 
  pinMode(10, INPUT);
  Serial.begin(9600);
  towerprosg5010.attach(9); 
  towerprosg5010.write(0);
  setTime(20, 59, 50, 27, 5, 2022);
  hora = now();
}
 
void loop() {
  if (hour()>=6){
    if (hour()<=21){
       val = digitalRead(PIR);
       if (val == HIGH){ 
          digitalWrite(LED, HIGH);  
          delay(4000);
          if (PirState == LOW){
            Serial.println("Sensor PIR activado");
            PirState = HIGH;
          }
       } 
       else{
          digitalWrite(LED, LOW); 
          if (PirState == HIGH){
            Serial.println("Sensor PIR parado");
            PirState = LOW;
          }
       }
      }else{  
        }
  }else{   
    }
  digitalWrite(11,LOW);
  delayMicroseconds(10);
  digitalWrite(11, HIGH);
  delayMicroseconds(10);
  tiempo=pulseIn(10, HIGH);
  distancia= (0.017*tiempo);
  if(distancia <= 15 && distancia!= 0){
    Serial.println("Caneca abierta");
    towerprosg5010.write(180);
    delay(4000);  
     Serial.println("Caneca cerrada");
    towerprosg5010.write(0);                               
  }
  Serial.print("Distancia: ");
  Serial.print(distancia);     
  Serial.print("cm");
  Serial.println();
  delay(2000); 
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)){
  Serial.println("Fallo en la lectura del sensor DHT!");
    return;
  }
    
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" *C\t ");    
}



//#include <SoftwareSerial.h>
//
//SoftwareSerial miBT(1,0);
//
//void setup()
//{
//  Serial.begin(9600);
//  Serial.println("listo");
//  miBT.begin(38400);
//}
//
//void loop()
//{
//  if(miBT.available())
//  Serial.write(miBT.read());
//
//  if(Serial.available())
//  miBT.write(Serial.read());
//}
