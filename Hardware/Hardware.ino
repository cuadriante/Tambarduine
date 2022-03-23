// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

#include <Servo.h>

int input_value = 10;

Servo servoHorizontal;

void setup() {
  servoHorizontal.attach(9);

  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  if (Serial.available()) {
    input_value = Serial.readString().toInt();
  }
  else{
    if (input_value == 1) {
      servoHorizontal.write(0);
    }
    else if (input_value == 2){
      alternarDireccion(servoHorizontal, 500);
    }
  }
}

void alternarDireccion(Servo servo, int velocidadGiro) {
  servo.write(0);
  delay(velocidadGiro);
  servo.write(180);
  delay(velocidadGiro);
}











void led_on() {
  digitalWrite(8, HIGH);
}

void led_off() {
  digitalWrite(8, LOW);
}

void controlarLed() {
  while (!Serial.available()); // No hace nada hasta que no se abra el puerto serial
  input_value = Serial.readString().toInt(); // Lee el valor recibido y lo convierte a int
  if (input_value == 1) {
    led_on();
  } else {
    led_off();
  }
}
