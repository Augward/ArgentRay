#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classNumber
Author: Augustin Ward
Created: 2025-16-03
Version: 1.2
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
        
        if type(number) != int and type(number) != float:
            raise TypeError("number must be: int, float, or Number")
        
        isNegative = -1 if number < 0 else 1
        number = abs(number)
        
        if type(element) == int:
            if element >= 2 and element <= 16:
                self.number = int(max(0, math.floor(number)))
                self.numType = "W"
                
                self.ogBase = element
                self.base = element
                
                self.number = int(self.convertBase(10)) * isNegative
                self.base = 10
                
            else:
                raise ValueError("base must be: >= 2, and <= 16")
        
        
        elif type(element) == str:
            if len(element) == 1:
                self.ogBase = None
                self.base = 10
                
                if element == "N":
                    self.number = int(max(1, math.floor(number)))
                    self.numType = "N"
                    
                elif element == "W":
                    self.number = int(max(0, math.floor(number)))
                    self.numType = "W"
                    
                elif element == "Z":
                    self.number = int(math.floor(number)) * isNegative
                    self.numType = "Z"
                    
                elif element == "Q":
                    self.number = round(float(number),12) * isNegative
                    self.numType = "Q"
                    
                elif element == "I":
                    self.number = float(number) * isNegative
                    self.numType = "I"
                    
                elif element == "C":
                    self.number = complex(number) * isNegative
                    self.numType = "C"
                    
                elif element == "R":
                    self.number = number * isNegative
                    self.numType = "R"
                
                else:
                    raise ValueError("numType must be: N, W, Z, Q, I, C, or R")
                    
            else:
                raise ValueError("numType must be only one character long")
        
        
        elif type(element) == None:
            self.number = number * isNegative
            self.numType = "R"
            self.base = 10
            
            
        else:
            raise TypeError("element must be int, str, or None")




    def __str__(self):
        return str(self.number) + ", Type: " + str(self.numType) + ", Original Base: " + str(self.ogBase if self.ogBase else self.base)




    def __add__(self, other):
        self.number + other.number
        
        
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
            return decimal
            
        isNegative2 = -1 if decimal < 0 else 1
        decimal = abs(decimal)
            
            
        digits = "0123456789ABCDEF"
        result = ""
        while decimal > 0:
            result = digits[decimal % newBase] + result
            decimal //= newBase
        
        return int(result) * isNegative2 if newBase <= 10 else str("-" if isNegative2 == -1 else "") + result
        
        


'''
x = Number(-16, 16)
print(x)
x3 = x.number
x4 = x.convertBase(14)
x5 = x.numType
x6 = x.base

y = Number(-44.4, "R")
print(y)
y2 = y.convertBase(8)
y3 = y.numType
y4 = y.number

z = Number(y2, 8)
print(z)
'''
