import time
import serial  # pip install pyserial

# Hay que poner el puerto al que esta conectado el arduino

signal = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
metronomo = 0.75


def iniciar_comunicacion():
    signal.write(bytes('<0>', 'utf-8'))
    time.sleep(1)


def set_metronomo(tiempo_entre_golpes):
    global metronomo
    metronomo = tiempo_entre_golpes

    signal.write(bytes('<1$' + str(metronomo) + '>', 'utf-8'))
    time.sleep(metronomo)


def abanicoA():
    signal.write(bytes('<2>', 'utf-8'))
    time.sleep(metronomo)


def abanicoB():
    signal.write(bytes('<3>', 'utf-8'))
    time.sleep(metronomo)


def verticalD():
    signal.write(bytes('<4>', 'utf-8'))
    time.sleep(metronomo)


def verticalI():
    signal.write(bytes('<5>', 'utf-8'))
    time.sleep(metronomo)


def percutorD():
    signal.write(bytes('<6>', 'utf-8'))
    time.sleep(metronomo)


def percutorI():
    signal.write(bytes('<7>', 'utf-8'))
    time.sleep(metronomo)


def percutorDI():
    signal.write(bytes('<8>', 'utf-8'))
    time.sleep(metronomo)


def percutorA():
    signal.write(bytes('<9>', 'utf-8'))
    time.sleep(metronomo)


def percutorB():
    signal.write(bytes('<10>', 'utf-8'))
    time.sleep(metronomo)


def percutorAB():
    signal.write(bytes('<11>', 'utf-8'))
    time.sleep(metronomo)


def golpe():
    signal.write(bytes('<12>', 'utf-8'))
    time.sleep(metronomo)


def vibrato_vertical(cantidad_de_repeticiones):
    signal.write(bytes('<13$' + str(cantidad_de_repeticiones) + '>', 'utf-8'))
    time.sleep(cantidad_de_repeticiones * metronomo)
