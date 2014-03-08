#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gonzalo Chacaltana Buleje <gchacaltanab@outlook.com>
from math import floor
import time

class DateProcessing(object):

    first_month = 1
    last_month = 12

    def __init__(self):
        pass

    """
    day of week, return number day of week, sunday = 0
    """
    def day_week(self, year, month, day):
 
        d = day
        m = (month - 3) % 12 + 1
        if m > 10: 
            Y = year - 1
        else: 
            Y = year

        y = Y % 100
        c = (Y - (Y % 100)) / 100
 
        w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
 
        return int(w)
 
    """
    list day of a date range
    """
    def calculate_sunday_by_range(self,year_start,year_end):
        #sunday's counter
        sundays = 0
        
        for year in range(year_start, year_end + 1):
            for month in range(self.first_month,self.last_month + 1):
                if self.day_week(year, month, 1) == 0: sundays += 1
        
        return sundays
 
if __name__ == "__main__" :
    
    year_start = 1901
    year_end = 2000
    
    date = DateProcessing()
    sundays = date.calculate_sunday_by_range(year_start, year_end)
 
    print "El número de domingos que cayó como primer día del mes, entre %s y %s fueron de : %s veces" % (year_start,year_end,sundays)
