# Programa que devuelve suma acumulada antes de sobrepasar los 10000
# @author: Gonzalo Chacaltana B <gchacaltanab@gmail.com>
import random

def ramdon_accumulate(limite):
    """Funcion que devuelve suma acumulada"""
    suma = 0
    value = 0

    while suma < limite:
        value = random.randint(1, 100)
        suma+=value

    return suma - value

suma = ramdon_accumulate(10000)
print "Suma acumulada : " + str(suma)