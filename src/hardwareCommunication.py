import time
import serial  # pip install pyserial

# Hay que poner el puerto al que esta conectado el arduino

signal = serial.Serial('/dev/ttyACM0', 9600)
communicating = False


def stop_communication():
    global communicating
    communicating = False


def start_communication():
    global communicating
    communicating = True


def detener_servo():
    start_communication()
    signal.write(bytes('1', 'utf-8'))
    stop_communication()


def alternar_direccion_servo():
    start_communication()
    signal.write(bytes('2', 'utf-8'))
    stop_communication()
