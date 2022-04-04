import time
import serial

#puertoSerial = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)
metronomo = 0
instrucciones = ''


def set_metronomo(tiempo_entre_golpes):
    global metronomo
    metronomo = tiempo_entre_golpes

    global instrucciones
    if metronomo != 0:
        instrucciones += ('<1$' + str(metronomo) + '>')


def unset_metronomo(tiempo_entre_golpes):
    global metronomo
    metronomo = tiempo_entre_golpes

    global instrucciones
    if metronomo != 0:
        instrucciones += ('<14$' + str(metronomo) + '>')


def abanicoA():
    global instrucciones
    instrucciones += ('<2>')


def abanicoB():
    global instrucciones
    instrucciones += ('<3>')


def verticalD():
    global instrucciones
    instrucciones += ('<4>')


def verticalI():
    global instrucciones
    instrucciones += ('<5>')


def percutorD():
    global instrucciones
    instrucciones += ('<6>')


def percutorI():
    global instrucciones
    instrucciones += ('<7>')


def percutorDI():
    global instrucciones
    instrucciones += ('<8>')


def percutorA():
    global instrucciones
    instrucciones += ('<9>')


def percutorB():
    global instrucciones
    instrucciones += ('<10>')


def percutorAB():
    global instrucciones
    instrucciones += ('<11>')


def golpe():
    global instrucciones
    instrucciones += ('<12>')


def vibrato_vertical(cantidad_de_repeticiones):
    global instrucciones
    instrucciones += ('<13$' + str(cantidad_de_repeticiones) + '>')


def enviar_instrucciones():
    global instrucciones
    print(instrucciones)
#    puertoSerial.write(bytes(instrucciones, 'utf-8'))
    instrucciones = ''
    time.sleep(3)
