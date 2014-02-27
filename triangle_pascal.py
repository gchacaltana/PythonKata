#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa que devuelve el triángulo de pascal en Python.
# @author: Gonzalo Chacaltana Buleje <gchacaltanab@outlook.com>

#importamos el paquete sys para obtener los valores argv enviados por consola.
import sys

def triangle_pascal(rows):
    """Funcion que recibe como parametro el número de filas del triángulo"""
    #si el número de filas es cero devolvemos vacío.
    if rows == 0:
        return []
    #si el número de filas es 1, devolvemos triangulo con una sola fila.
    elif rows == 1:
        return [[1]]
    else:
    #de lo contrario armamos el triángulo segun el número de filas
        new_row = [1]
        #llamamos nuevamente a la función para armar el triángulo
        result = triangle_pascal(rows-1)
		#guardamos la última fila.
        last_row = result[-1]
		#iteramos la cantidad de veces del valor de filas - 1.
        for i in range(len(last_row)-1):
			#agregamos los valores a la nueva fila.
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        #agregamos a la matriz del triángulo la nueva fila
        result.append(new_row)
	#devolvemos el array con los valores del triángulo.
    return result

#main del programa
if __name__ == "__main__":
    #almacenamos el número de filas enviado como argumento por consola
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else int(0)
    
    #mostramos el triángulo con el número de filas enviado.
    print triangle_pascal(rows)
