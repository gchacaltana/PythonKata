#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Gonzalo Chacaltana Buleje'

def main():
    #obtenemos los numberos multiplos de 3 y 5
    numbers = [n for n in xrange(1,1000) if (n%3==0)or(n%5==0)]
    #mostramos la suma
    suma = sum(numbers)
    print "La suma de todos los multiplos de 3 y 5 hasta 1000 es: " % suma

if __name__ == '__main__':
    main()
