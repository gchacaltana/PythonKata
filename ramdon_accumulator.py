#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa que devuelve suma acumulada antes de sobrepasar los 10000
# @author: Gonzalo Chacaltana Buleje <gchacaltanab@outlook.com>
import random

def ramdon_accumulate(limite):
    """Función que devuelve suma acumulada"""
    suma = 0
    value = 0

    while suma < limite:
        value = random.randint(1, 100)
        suma+=value

    return suma - value

# main del programa
if __name__ == "__main__":

    suma = ramdon_accumulate(10000)
    print "Suma acumulada : " + str(suma)

