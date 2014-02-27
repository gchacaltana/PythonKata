#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa que devuelve cadena invertida en secciones de cabeza y cola.
# @author: Gonzalo Chacaltana Buleje <gchacaltanab@outlook.com>

#importamos el paquete sys para obtener los valores argv enviados por consola.
import sys

def recursive_reverse(param):
    """ Funcion para invertir cadena en cabeza y cola
    """
    cabeza = param[0:1]
    cola = param[1:len(param)]
    return cola + cabeza


# main del programa
if __name__ == "__main__":
    #almacenamos el valor enviado como parametro en la consola.
#    param = str(sys.argv[1]) if (sys.argv[1]) else " "
    if len(sys.argv) > 1:
        param = sys.argv[1]
    else:
        param = " "

    print recursive_reverse(param)


