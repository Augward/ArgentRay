#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classNumber
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0.1
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
        
# TODO: →
    # Used for Sets and Discrete math
        
    # Union and other discrete math functions maybe included
    
    # Convert between bases of 2, 4, 8, 10, 16
"""
import math
import cmath

class Number:
    # N = Natural (0,1,2), Z = Integer (-1,0,1), R = Real (-pi, 0, pi)
    # Q = Rational (0.5, 1/2, 1/9), I = Irrational (unable), C = Complex (ai + b)
    # Base saved = 2, 4, 8, 10, 16; able to compute any base
    def __init__(self, number, numType = "R", base = 10):
        self.number = number
        self.numType = numType
        self.base = base
        
        if numType == "N":
            self.number = int(max(0, math.floor(number)))
        elif numType == "Z":
            self.number = int(math.floor(number))
        elif numType == "Q":
            self.number = float(number)
        elif numType == "I":
            self.number = float(number)
        elif numType == "C":
            self.number = complex(number)
        else:
            self.numType = "R"
            
        self.base2 = self.convertBase(2)
        self.base4 = self.convertBase(4)
        self.base8 = self.convertBase(8)
        self.base10 = self.convertBase(10)
        self.base16 = self.convertBase(16)
            
            
            
            
    def convertBase(self, newBase):
        if self.numType == "N" or self.numType == "Z":
            if self.base == newBase:
                return self.number
            
            if self.base != 10:
                decimal = int(str(self.number), self.base)
            else:
                decimal = int(self.number)
            
            if newBase == 10:
                return decimal
            
            
            digits = "0123456789ABCDEF"
            result = ""
            while decimal > 0:
                result = digits[decimal % newBase] + result
                decimal //= newBase
            
            return int(result) if result else 0
        else:
            raise ValueError("Must be Natural (N) or Integer (Z) to change base")
        
        


x = Number(17, "Z", 10)
print(x.base2)
print(x.convertBase(11))
