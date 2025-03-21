#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classNumber
Author: Augustin Ward
Created: 2025-16-03
Version: 1.3
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
"""
import math
import cmath

class Number:
    # N = Natural (1,2,3), W = Whole (0,1,2), Z = Integer (-1,0,1), R = Real (-pi, 0, pi)
    # Q = Rational (0.5, 1/2, 1/9), I = Irrational (unable), C = Complex (ai + b)
    # Base saved = 2, 4, 8, 10, 16; able to compute any base
    
    def __init__(self, number, element = None):
        
        self.ogNumber = number
        
        if not isinstance(number, (int, float, str)):
            raise TypeError("number must be: int, float, or str")        
        
        
        if isinstance(element, int):
            if 2 <= element <= 16:
                self.ogBase = element
                self.base = element
                
                if not isinstance(number, str):
                    number = int(math.floor(number))
                    
                    isNegative = -1 if number < 0 else 1
                    self.number = abs(number)
                    
                    self.number = int(self.convertBase(10)) * isNegative
                    
                else:
                    isNegative = -1 if (number[0] == "-") else 1
                    self.number = number.lstrip("-")
                    
                    self.number = int(self.number, self.base) * isNegative
                
                self.numType = "W"
                self.base = 10
                
            else:
                raise ValueError("base must be: >= 2, and <= 16")
            
            
        elif isinstance(element, str):
            self.ogBase = 10
            self.base = 10
            
            if len(element) == 1:
                if element == "N":
                    self.number = int(max(1, math.floor(number)))
                    self.numType = "N"
                    
                elif element == "W":
                    self.number = int(max(0, math.floor(number)))
                    self.numType = "W"
                    
                elif element == "Z":
                    self.number = int(math.floor(number))
                    self.numType = "Z"
                    
                elif element == "Q":
                    self.number = round(float(number),12)
                    self.numType = "Q"
                    
                elif element == "I":
                    self.number = float(number)
                    self.numType = "I"
                    
                elif element == "C":
                    self.number = complex(number)
                    self.numType = "C"
                    
                elif element == "R":
                    self.number = number
                    self.numType = "R"
                
                else:
                    raise ValueError("numType must be: N, W, Z, Q, I, C, or R")
                    
            else:
                raise ValueError("numType must be only one character long")
        
        
        elif element == None:
            self.number = number
            self.numType = "R"
            self.ogBase = 10
            self.base = 10
            
            
        else:
            raise TypeError("element must be int, str, or None")




    def __str__(self):
        return str(self.number) + ", Type: " + str(self.numType) + ", Original Base: " + str(self.ogBase if self.ogBase else self.base)




    def __add__(self, other):
        self.number + other.number # Not done
        
        
    def __radd__(self, other):
        return self + other
        
        
        
        
        
    def convertBase(self, newBase):
        if self.base == newBase:
            return self.number
        
        if self.base != 10:
            decimal = int(str(self.number), self.base)
        else:
            decimal = int(self.number)
        
        if newBase == 10:
            return int(decimal)
            
        isNegative2 = -1 if decimal < 0 else 1
        decimal = abs(decimal)
            
        digits = "0123456789ABCDEF"
        result = ""
        while decimal > 0:
            result = digits[decimal % newBase] + result
            decimal //= newBase
        
        return int(result) * isNegative2 if newBase <= 10 else str("-" if isNegative2 == -1 else "") + result
        
        


'''
x = Number("-1E", 16)
print(x)
x2 = x.number
x3 = x.ogNumber
x4 = x.numType
x5 = x.base
x6 = x.ogBase

y = Number(-44.4, "Z")
print(y)
y2 = y.number
y3 = y.ogNumber
y4 = y.numType
y5 = y.base
y6 = y.ogBase

'''

'''
englishLength = {'in':1, 'ft':12, 'yd':36, 'mi':6360}
metricLength = {'mm':0.001, 'cm': 0.01, 'dm': 0.1, 'm':1, 'dam':10, 'hm':100, 'km':100}
lengthConversionME = x * 39.37/12 # meter to foot
lengthConversionEM = x * 12/39.37 # foot to meter

units = {'in':1, 'ft':12, 'yd':36, 'mi':6360, 'mm':0.001, 'cm': 0.01, 'dm': 0.1, 'm':1, 'dam':10, 'hm':100, 'km':100}
'''
