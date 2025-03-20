#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classPoint
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0.1
Description: Class that establishes a Point in 2D or 3D Space

License: NA
Contact: ward31513@gmail.com
Dependencies: math, cmath

'''
    |Points → 
        Array of points in a dictionary
        Single Point: Coordanite → (0,0)
        Two Points: Line → {(0,0), (1,1)}
        More Points on Same Plane: 2D Shape → {(0,0), (0,1), (1,0)}
        More Points in 3 Dimensions: 3D Shape → {(0,0,0), (1,0,0), (0,1,0), (0,0,1)}
"""
import math
import cmath

class Point:
    """========================================================================
    Description: 
        
        
    Attributes:
        
    ========================================================================"""
    def __init__(self, x = 0, y = 0, z = None):
        
        self.size = 2 + (z != None)
        
        if type(x) == int or type(x) == float:
            self.x = round(x,12)
            
        if type(y) == int or type(y) == float:
            self.y = round(y,12)
        
        if type(x) == int or type(x) == float:
            if z != None:
                self.z = round(z,12)
            else:
                self.z = 0
        
        self.list = [self.x, self.y, self.z]

        
        
        
        
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
       
    ========================================================================"""
    def __str__(self):
        if self.size == 3:
            if (self.x == 0) and (self.y == 0) and (self.z == 0):
                return "Origin → Size: 0"
            else:
                return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ") → Size: 3"
        else:
            if (self.x == 0) and (self.y == 0):
                return "Origin → Size: 0"
            elif self.x == 0:
                return "y = " + str(self.y) + " → Size: 1"
            elif self.y == 0:
                return "x = " + str(self.x) + " → Size: 1"
            else:
                return "(" + str(self.x) + "," + str(self.y) + ") → Size: 2"
                
        
        
        
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
       
    ========================================================================"""
    def __add__(self, other):
        if type(other) == Point:
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            
            return Point(x, y, z)
        
    
    def __radd__(self, other):
        return self + other
    
    
    
    
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
       
    ========================================================================"""
    def __sub__(self, other):
        if type(other) == Point:
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
            
            return Point(x, y, z)
        
    
    def __rsub__(self, other):
        return self - other
    
    
    
    
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
       
    ========================================================================"""
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            x = self.x * other
            y = self.y * other
            z = self.z * other
        else:
            raise ValueError("Other needs to be a number")
        
        return Point(x, y, z)
    
    
    def __rmul__(self, other):
        return self * other
    
    
    
    
    
# Dot product

# Cross product


    
    
        
point = Point(1,2,3)
print(point)

point2 = Point(1.2,2.6,7.8)
print(point2)

point3 = point - point2
print(point3.list)

point4 = 3 * point3
print(point4)
