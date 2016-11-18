# coding: utf-8
# proyecto 1
import random


numero = 69

while True:
    adivinanza = input("Introduce un numero: ")
    if adivinanza == numero:
        print("Enhorabuena has acertado el numero {0}".format(numero))
    elif adivinanza < numero:
	print("El numero es mas alto")
    else:
	print("El numero es mas bajo")
