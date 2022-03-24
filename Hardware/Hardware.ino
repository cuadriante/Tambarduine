// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>

int input_value = 99;
float metronomo = 500;

Servo servoVertical;
Servo servoAbanico;

void setup() {
  servoVertical.attach(9);
  servoAbanico.attach(10);
  setMetronomo(0.75);

  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  verticalD();
  delay(1000);
  abanicoA();
  delay(1000);
  verticalI();
  delay(1000);
  abanicoB();
  delay(1000);
/*  if (Serial.available()) {
    input_value = Serial.readString().toInt();
  }
  else{
    if (input_value == 1) {
      servoHorizontal.write(0);
    }
    else if (input_value == 2){
      alternarDireccion(servoHorizontal, 500);
    }
  }*/
}

void abanicoA(){
  servoAbanico.write(0);
  delay(metronomo);
  servoAbanico.write(90);
  servoAbanico.write(180);
  delay(metronomo);
  servoAbanico.write(90);
}

void abanicoB(){
  servoAbanico.write(180);
  delay(metronomo);
  servoAbanico.write(90);
  servoAbanico.write(0);
  delay(metronomo);
  servoAbanico.write(90);
}

void verticalD(){
  servoVertical.write(0);
  delay(metronomo);
  servoVertical.write(90);
  servoVertical.write(180);
  delay(metronomo);
  servoVertical.write(90);
}

void verticalI(){
  servoVertical.write(180);
  delay(metronomo);
  servoVertical.write(90);
  servoVertical.write(0);
  delay(metronomo);
  servoVertical.write(90);
}

void setMetronomo(float tiempoEntreGolpes){
  metronomo = tiempoEntreGolpes/2 * 1000;
}
