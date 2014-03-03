#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Gonzalo Chacaltana Buleje'

def main():

    #numero a hallar mayor factor primo
    number = 600851475143
    i = 2
    factor = 0
    n = number

    while n > 1:
      if n % i == 0:
        if factor < i:
            factor = i
        n = n / i
        i = 2
      else:
          i = i + 1

    #mostramos el mayor número primo
    print "El mayor factor primo es:  %s" %factor

if __name__ == '__main__':
    main()
