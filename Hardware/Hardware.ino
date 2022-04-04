// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>

int funcionLlamada = 0;
float parametroFuncion = 0;

const byte cantidadCaracteres = 32;
char mensaje[cantidadCaracteres];

float tempo = 400;
bool metronomoActivo = true;
int tiempoSonido = 100;
int anguloInicialPercutores = 155;

Servo servoPercutorA;
Servo servoPercutorB;
Servo servoPercutorD;
Servo servoPercutorI;
Servo servoPercutorC;

Servo servoVertical;
Servo servoAbanico;

void setup() {
  pinMode(9, OUTPUT);

  servoPercutorA.attach(2);
  servoPercutorB.attach(3);
  servoPercutorD.attach(4);
  servoPercutorI.attach(5);
  servoPercutorC.attach(6);

  servoAbanico.attach(7);
  servoVertical.attach(8);

  posicionarPercutores(anguloInicialPercutores);

  setMetronomo(0.75);

  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  recibirInstruccion();
  
  if (funcionLlamada == 1) {
    setMetronomo(parametroFuncion);
  }
  else if (funcionLlamada == 2){
    girarSentidoHorario(servoAbanico); //abanicoA
  }
  else if (funcionLlamada == 3){
    girarSentidoAntihorario(servoAbanico); //abanicoB
  }
  else if (funcionLlamada == 4){
    girarSentidoHorario(servoVertical); //verticalD
  }
  else if (funcionLlamada == 5){
    girarSentidoAntihorario(servoVertical); //verticalI
  }
  else if (funcionLlamada == 6){
    usarPercutor(servoPercutorD);
  }
  else if (funcionLlamada == 7){
    usarPercutor(servoPercutorI);
  }
  else if (funcionLlamada == 8){
    usarPercutores(servoPercutorD, servoPercutorI);
  }
  else if (funcionLlamada == 9){
    usarPercutor(servoPercutorA);
  }
  else if (funcionLlamada == 10){
    usarPercutor(servoPercutorB);
  }
  else if (funcionLlamada == 11){
    usarPercutores(servoPercutorA, servoPercutorB);      
  }
  else if (funcionLlamada == 12){
    usarPercutor(servoPercutorC);
  }
  else if (funcionLlamada == 13){
    vibrato(parametroFuncion);
  }
  else if (funcionLlamada == 14){
    unsetMetronomo(parametroFuncion);
  }
  else{
    detenerServos();
  }
  funcionLlamada = 0;
  parametroFuncion = 0;
}

void recibirInstruccion() {
  static boolean recibiendoMensaje = false;
  static byte pos = 0;
  char marcadorInicio = '<';
  char marcadorFinal = '>';
  char caracterRecibido;
  bool recepcionCompleta = false;
  
  while (Serial.available() > 0 && recepcionCompleta == false) {
    caracterRecibido = Serial.read();

    if (recibiendoMensaje) {
      if (caracterRecibido != marcadorFinal) {
        mensaje[pos] = caracterRecibido;
        pos++;
        if (pos >= cantidadCaracteres) {
          pos = cantidadCaracteres - 1;
        } 
      }
      else {
        mensaje[pos] = '\0';
        recibiendoMensaje = false;
        pos = 0;
        recepcionCompleta = true;
        procesarMensaje(mensaje);
      }
    }
    else if (caracterRecibido == marcadorInicio) {
      recibiendoMensaje = true;
    }
  }
}

void procesarMensaje(char mensajeRecibido[]){
  Serial.println(mensajeRecibido);
  char marcadorDeSeparacion = '$';
  String mensajeString = mensajeRecibido;
  
  for (int i = 0; i < mensajeString.length(); i++){
    char caracter = mensajeRecibido[i];
    if (caracter == marcadorDeSeparacion){
      funcionLlamada = mensajeString.substring(0, i).toInt();
      parametroFuncion = mensajeString.substring(i + 1, mensajeString.length()).toFloat();
      break;
    }
    else{
      funcionLlamada = mensajeString.toInt();
    }
  }
}

void detenerServos() {
  servoAbanico.write(90);
  servoVertical.write(90);
}

void posicionarPercutores(int angulo) {
  servoPercutorA.write(angulo);
  servoPercutorB.write(angulo);
  servoPercutorD.write(angulo);
  servoPercutorI.write(angulo);
  servoPercutorC.write(angulo);
  delay(500);
}

void setMetronomo(float tiempoEntreGolpes) {
  tempo = tiempoEntreGolpes / 2 * 1000;
  metronomoActivo = true;
}

void unsetMetronomo(float tiempoEntreGolpes) {
  tempo = tiempoEntreGolpes / 2 * 1000;
  metronomoActivo = false;
}

void sonarMetronomo() {
  if(metronomoActivo){
    tone(9, 1000);
  }
  delay(tiempoSonido); 
  noTone(9);
}

void girarSentidoHorario(Servo servo){
  servo.write(0);

  delay(tempo);

  servo.write(180);
  sonarMetronomo();

  delay(tempo - tiempoSonido);

  servo.write(90);
}

void girarSentidoAntihorario(Servo servo){
  servo.write(180);

  delay(tempo);

  servo.write(0);
  sonarMetronomo();

  delay(tempo - tiempoSonido);

  servo.write(90);
}

void usarPercutor(Servo percutor) {
  int angulo = anguloInicialPercutores;
  int anguloFinal = anguloInicialPercutores - 90;
  while (angulo != anguloFinal) {
    angulo -= 1;
    percutor.write(angulo);
    delay(tempo / 90);
  }

  sonarMetronomo();

  while (angulo != anguloInicialPercutores) {
    angulo += 1;
    percutor.write(angulo);
    delay((tempo - tiempoSonido) / 90);
  }
}

void usarPercutores(Servo primerPercutor, Servo segundoPercutor) {
  int angulo = anguloInicialPercutores;
  int anguloFinal = anguloInicialPercutores - 90;
  while (angulo != anguloFinal) {
    angulo -= 1;
    primerPercutor.write(angulo);
    segundoPercutor.write(angulo);
    delay(tempo / 90);
  }

  sonarMetronomo();

  while (angulo != anguloInicialPercutores) {
    angulo += 1;
    primerPercutor.write(angulo);
    segundoPercutor.write(angulo);
    delay((tempo - tiempoSonido) / 90);
  }
}

void vibrato (int cantidadDeRepeticiones) {
  int i = 0;
  while (i < cantidadDeRepeticiones) {
    girarSentidoHorario(servoVertical);
    girarSentidoAntihorario(servoVertical);
    i += 1;
  }
}
