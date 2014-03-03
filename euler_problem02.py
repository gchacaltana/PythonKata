#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Gonzalo Chacaltana Buleje'

def main():
    #valores iniciales.
    number = 1
    limit = 4000000
    l = [1,1]
    while (number <= limit):
        number = l[len(l)-1]+l[len(l)-2]
        l.append(number)

    #retornamos la suma de los números.
    suma = sum([n for n in l if(n%2==0)])
    print "La suma de los números es: %s" % suma

if __name__ == '__main__':
    main()
