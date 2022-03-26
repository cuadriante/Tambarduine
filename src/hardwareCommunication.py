import time
import serial  # pip install pyserial

# Hay que poner el puerto al que esta conectado el arduino

signal = serial.Serial('/dev/ttyACM0', 9600)
metronomo = 0.75


def set_metronomo(tiempo_entre_golpes):
    metronomo = tiempo_entre_golpes
    signal.write(bytes('1', 'utf-8'))
    time.sleep(1)


def abanicoA():
    signal.write(bytes('2', 'utf-8'))
    time.sleep(metronomo)


def abanicoB():
    signal.write(bytes('3', 'utf-8'))
    time.sleep(metronomo)


def verticalD():
    signal.write(bytes('4', 'utf-8'))
    time.sleep(metronomo)


def verticalI():
    signal.write(bytes('5', 'utf-8'))
    time.sleep(metronomo)


def percutorD():
    signal.write(bytes('6', 'utf-8'))


def percutorI():
    signal.write(bytes('7', 'utf-8'))


def percutorDI():
    signal.write(bytes('8', 'utf-8'))


def percutorA():
    signal.write(bytes('9', 'utf-8'))


def percutorB():
    signal.write(bytes('A', 'utf-8'))


def percutorAB():
    signal.write(bytes('B', 'utf-8'))


def golpe():
    signal.write(bytes('C', 'utf-8'))


def vibrato_vertical(cantidad_de_repeticiones):
    signal.write(bytes('D', 'utf-8'))
    time.sleep(2 * cantidad_de_repeticiones * metronomo)
