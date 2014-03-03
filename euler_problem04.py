#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Gonzalo Chacaltana Buleje'

def capicua(n):
    s = str(n)
    return s == s[::-1]

def main():
    first_number, second_number, capicua_number = 0,0, 0
    for x in xrange(999,99,-1):
        for y in xrange(x, 99,-1):
            if x*y < capicua_number: continue
            if capicua(x*y):
                first_number, second_number, capicua_number = x,y, x*y

    print "El primer número 3 dígitos: %s" % first_number
    print "El segundo número 3 dígitos: %s" % second_number
    print "El mayor número capicua de 3 dígitos es : %s" % capicua_number


if __name__ == '__main__':
    main()
