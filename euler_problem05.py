#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Gonzalo Chacaltana Buleje'

def is_divisible(n):
    if n < 1:
        return False
    elif n == 1:
        return 1
    else:
        step = is_divisible(n-1)
        number = 0
        found = False
        while not found:
            number += step
            found = is_divisible_to(number, n)
        return number

def is_divisible_to(number, x):
    for i in reversed(range(1, x+1)):
        if number % i != 0:
            return False
    return True

if __name__ == '__main__':
    print "El menor número divisible entre 1 a 20 es : %s" % is_divisible(20)
