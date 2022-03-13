import os
import serial  # pip install pyserial

os.system('cls || clear')

# Hay que poner el puerto al que esta conectado el arduino
signal = serial.Serial('/dev/ttyACM0', 9600)


def led_on():
    signal.write(bytes('1', 'utf-8'))  # Envia un string '1' al arduino


def led_off():
    signal.write(bytes('0', 'utf-8'))  # Envia un string '0' al arduino


communicating = True
while (communicating):
    # Si pone un 0 apaga el led, si pone un 1 lo enciende, si pone
    # cualquier otra cosa lo apaga y deja de comunicarse con el arduino
    input_number = input('Enter a number: ')

    try:
        input_number = int(input_number)
    except:
        input_number = None
    finally:
        if (input_number == 0):
            led_off()
        elif (input_number == 1):
            led_on()
        else:
            led_off()
            signal.close()
            communicating = False
            print('Communication closed')
