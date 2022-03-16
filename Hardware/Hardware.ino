// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>

int input_value;

Servo servoHorizontal;

void setup() {
  servoHorizontal.attach(9);


  
  pinMode(8,  OUTPUT);
  digitalWrite(8, LOW);
  
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  //alternarDireccion(servoHorizontal, 750);
}

void alternarDireccion(Servo servo, int tiempoDeGiro){
  servo.write(0);
  delay(tiempoDeGiro);
  servo.write(180);
  delay(tiempoDeGiro);
}











void led_on(){
  digitalWrite(8, HIGH);
}

void led_off(){
  digitalWrite(8, LOW);
}

void controlarLed(){
  while (!Serial.available()); // No hace nada hasta que no se abra el puerto serial
  input_value = Serial.readString().toInt(); // Lee el valor recibido y lo convierte a int
  if(input_value == 1){
    led_on();
  }else{
    led_off();
  }
}
