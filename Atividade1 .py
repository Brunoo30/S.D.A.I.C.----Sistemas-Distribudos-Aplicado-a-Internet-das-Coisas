from pyfirmata2 import Arduino
import random

PORTA = Arduino.AUTODETECT
arduino = Arduino(PORTA)

vermelho = arduino.get_pin('d:6:p')
azul = arduino.get_pin('d:9:p')
verde = arduino.get_pin('d:5:p')

def acender(cor, brilho):
    if cor == "vermelho":
        vermelho.write(brilho)
        azul.write(0)
        verde.write(0)
    elif cor == "verde":
        vermelho.write(0)
        azul.write(0)
        verde.write(brilho)
    elif cor == "azul":
        vermelho.write(0)
        azul.write(brilho)
        verde.write(0)
    elif cor == "apagar":
        vermelho.write(0)
        azul.write(0)
        verde.write(0)
    else: print("Cor invalida")

while True:
    cor = input("Digite a cor desejada (vermelho, verde, azul ou apagar): ")
    if cor == "apagar":
        acender(cor, 0)
    else:
        brilho = float(input("Digite a proporção de brilho (entre 0 e 1): "))
        acender(cor, brilho)
