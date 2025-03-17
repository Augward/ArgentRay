#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classNumber
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0
Description: Class that establishes a type of number

License: NA
Contact: ward31513@gmail.com
Dependencies: math, cmath

'''
    |Numbers →      Numbers are objects that can go inside other objects listed
        Imaginary Numbers: i
        Real Numbers: Any
            [Irrational/Radical Numbers: sqrt(3), pi]
            [Rational Numbers: 1.2,3/4,-5/8 
             [Integers: -1,0,1 
              [Whole Numbers: 0,1,2 
               [Natural Numbers: 1,2,3]]]]
"""
import math
import cmath

class Number:
    def __init__(self, number):
        self.number = number