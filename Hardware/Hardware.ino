// Para subir el código desde linux
// ls -l /dev/ttyACM*
// sudo chmod a+rw /dev/ttyACM0

int input_value;
void setup() {
  pinMode(8,  OUTPUT);
  digitalWrite(8, LOW);
  
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available()); // No hace nada hasta que no se abra el puerto serial
  input_value = Serial.readString().toInt(); // Lee el valor recibido y lo convierte a int
  if(input_value == 1){
    led_on();
  }else{
    led_off();
  }
}

void led_on(){
  digitalWrite(8, HIGH);
}

void led_off(){
  digitalWrite(8, LOW);
}
