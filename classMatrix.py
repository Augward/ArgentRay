#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classMatrix
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0.3
Description: Class that establishes a Matrix of some size

License: NA
Contact: ward31513@gmail.com
Dependencies: math, cmath

'''
    |Matrix →
        Arrays in an Array or Dictionary
"""
import math
import cmath

class Matrix:
    """========================================================================
    Description: 
        
        
    Attributes:
        
    ========================================================================"""
    def __init__(self, data = 1, second = 1):
        
        if type(data) == list: 
            self.rows = len(data)
            self.columns = max(len(row) for row in data) if self.rows > 0 else 0
            self.matrix = []
                        
            for row in data:
                while len(row) < self.columns:
                    row.append(0)
                self.matrix.append(row)
                
            [[round(self.matrix[i][j], 12) for i in range(self.columns)] for j in range(self.rows)]
            
        elif type(data) == int and type(second) == int:
            self.rows = data
            self.columns = second
            self.matrix = [[0] * second for i in range(data)]
        
        else:
            raise ValueError("Improper format to build matrix")
        
        self.size = [self.rows, self.columns]
        
        
        self.transpose = [[self.matrix[i][j] for i in range(self.rows)] for j in range(self.columns)]
        self.sizeTranspose = [self.columns, self.rows]
        
        
        self.isSquare = (self.rows == self.columns)
        self.sizeSquare = self.rows if self.isSquare else None
        
        
        if self.isSquare:
            if self.sizeSquare == 1:
                self.determinant = self.matrix[0][0]
                
            elif self.sizeSquare == 2:
                self.determinant = round((self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1]), 12)
                
            elif self.sizeSquare == 3:
                a = self.matrix[0][0] * ((self.matrix[1][1] * self.matrix[2][2]) - (self.matrix[2][1] * self.matrix[1][2]))
                b = self.matrix[0][1] * ((self.matrix[1][0] * self.matrix[2][2]) - (self.matrix[2][0] * self.matrix[1][2]))
                c = self.matrix[0][2] * ((self.matrix[1][0] * self.matrix[2][1]) - (self.matrix[2][0] * self.matrix[1][1]))
                self.determinant = round(a - b + c, 12)
                
            else:
                self.determinant = None
                print("Further determinant implementation required for sizes larger than 3x3")
                
        else:
            self.determinant = None
            
        
        
        
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
       
    ========================================================================"""
    def __str__(self):
        string = "\nMatrix:\n"
        for row in self.matrix:
            string += str(row) + "\n"
        string += "Size: " + str(self.size)
        return string
    
    
    def transpose__str(self):
        string = "\nTranspose Matrix:\n"
        for row in self.transpose:
            string += str(row) + "\n"
        string += "Size: " + str(self.sizeTranspose)
        return string
        
    
    
    
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
        
    ========================================================================"""
    def __add__(self, other):
        
        if type(other) != Matrix:
            raise ValueError("Matrices can only be added to other matrices")
        if (self.sizeSquare != other.sizeSquare):
            raise ValueError("Matrices must be the same size to be added")
    
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(data = result)
        
    
    def __radd__(self, other):
        return self + other
          
    
            
            
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
        
    ========================================================================"""        
    def __sub__(self, other):
        
        if type(other) != Matrix:
            raise ValueError("Matrices can only be added to other matrices")
        if (self.sizeSquare != other.sizeSquare):
            raise ValueError("Matrices must be the same size to be added")
    
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(data = result)
            
                  
    def __rsub__(self, other):
        return self - other
        
        
        
        
    """========================================================================
    Description: 
        
        
    Inputs:
        
        
    Outputs:
        
    ========================================================================"""    
    def __mul__(self, other):
        
        if type(other) == int or type(other) == float or type(other) == bool:
            result = [[other * self.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return Matrix(data = result)
            
        elif type(other) == Matrix:
            if self.columns != other.rows:
                raise ValueError("Matrix column must be equal to second matrix rows")
            
            result = []
            for i in range(self.rows):
                new = []
                for j in range(other.columns):
                    val = 0
                    for k in range(self.columns):
                        val += self.matrix[i][k] * other.matrix[k][j]
                    new.append(val)
                result.append(new)
            return Matrix(data=result)
            
        else:
            raise ValueError("Matrices can only be multiplied by matrices or numbers")
            
                
    def __rmul__(self, other):
        return self * other
    



y = Matrix()
print(y)

x = Matrix([[1,2,5],[2,2,5.01],[3,2,-1]])
print(x)
print(x.determinant)



    
    # Inverse
    
    # Row Echelon Form
    
    # Reduced Row Echelon Form
    
    # Diagonal Matrix
    
    # LU decomposition
    
    # Eignevalues
    
    # Eigenvectors
    
    
    
