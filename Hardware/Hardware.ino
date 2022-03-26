// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>

String input_value = "";
float metronomo;
int tiempoSonido = 100;

Servo servoVertical;
Servo servoAbanico;

Servo servoPercutorA;
Servo servoPercutorB;
Servo servoPercutorD;
Servo servoPercutorI;
Servo servoPercutorC;

void setup() {
  pinMode(8, OUTPUT);

  servoAbanico.attach(6);
  servoVertical.attach(7);

  servoPercutorA.attach(1);
  servoPercutorB.attach(2);
  servoPercutorD.attach(3);
  servoPercutorI.attach(4);
  servoPercutorC.attach(5);
  
  setMetronomo(0.75);

  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  if (Serial.available() > 1) {
    int message_max_length = 100;
    char python_message[message_max_length];
    int idx = 0;
    while (idx < message_max_length){
      python_message[idx] = Serial.read();
      idx += 1;
    }
    Serial.println(python_message[0]);
    Serial.println(python_message[1]);
    Serial.println(python_message[2]);
    Serial.println(python_message[3]);
  }
  else if (Serial.available() > 0){
    input_value = Serial.readString();
  }
  else{
    if (input_value == "1"){
      setMetronomo(0.3);
      input_value = "";
    }
      else if (input_value == "2"){
      abanicoA();
      input_value = "";
    }
      else if (input_value == "3"){
      abanicoB();
      input_value = "";
    }
      else if (input_value == "4"){
      verticalD();
      input_value = "";
    }
      else if (input_value == "5"){
      verticalI();
      input_value = "";
    }
      else if (input_value == "6"){
      percutorD();
      input_value = "";
    }
      else if (input_value == "7"){
      percutorI();
      input_value = "";
    }
      else if (input_value == "8"){
      percutorDI();
      input_value = "";
    }
      else if (input_value == "9"){
      percutorA();
      input_value = "";
    }
      else if (input_value == "A"){
      percutorB();
      input_value = "";
    }
      else if (input_value == "B"){
      percutorAB();
      input_value = "";
    }
      else if (input_value == "C"){
      golpe();
      input_value = "";
    }
      else if (input_value == "D"){
      vibrato(5);
      input_value = "";
    }
    else{
      detenerServos();
    }
  }
}

void detenerServos(){
  servoAbanico.write(90);
  servoVertical.write(90);
}

void setMetronomo(float tiempoEntreGolpes){
  metronomo = tiempoEntreGolpes/2 * 1000;
}

void abanicoA(){
  servoAbanico.write(180);
  
  delay(metronomo);
  
  servoAbanico.write(0);
  sonarMetronomo();

  delay(metronomo - tiempoSonido);

  servoVertical.write(90);
}

void abanicoB(){
  servoAbanico.write(0);
  
  delay(metronomo);

  servoAbanico.write(180);
  sonarMetronomo();
 
  delay(metronomo - tiempoSonido);

  servoVertical.write(90);
}

void verticalD(){
  servoVertical.write(0);
  delay(metronomo);

  servoVertical.write(180);
  sonarMetronomo();

  delay(metronomo - tiempoSonido);

  servoVertical.write(90);
}

void verticalI(){
  servoVertical.write(180);
  delay(metronomo);

  servoVertical.write(0);
  sonarMetronomo();
  
  delay(metronomo - tiempoSonido);

  servoVertical.write(90);
}

void percutorD(){
  
}

void percutorI(){

}

void percutorDI(){

}

void percutorA(){

}

void percutorB(){

}

void percutorAB(){

}

void golpe(){

}

void vibrato (int cantidadDeRepeticiones){
  int i = 0;
  while (i < cantidadDeRepeticiones){
    verticalD();
    verticalI();
    i += 1;
  }

}

void sonarMetronomo(){
  digitalWrite(8, HIGH);
  delay(tiempoSonido);
  digitalWrite(8, LOW);
}
