#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classMatrix
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0.1
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
    def __init__(self, rows = 1, columns = 1, data = None):
        
        if type(data) == list: 
            self.rows = len(data)
            self.columns = max(len(row) for row in data) if self.rows > 0 else 0
            self.matrix = []
            
            for row in data:
                while len(row) < self.columns:
                    row.append(0)
                self.matrix.append(row)
            
        else:
            self.rows = rows
            self.columns = columns
            self.matrix = [[0] * columns for i in range(rows)]


    def __str__(self):
        for row in self.matrix:
            print(row)
        return str(x.rows) + " x " + str(x.columns)
        

x = Matrix(2, 2, [[1],[1,1,1,1]])
print(x)

    # +
    
    # -
    
    # *
    
    # Determinant
    
    # Inverse
    
    # Transpose
    
    # Row Echelon Form
    
    # Reduced Row Echelon Form
    
    # Diagonal Matrix
    
    # LU decomposition
    
    # Eignevalues
    
    # Eigenvectors
    
    
    
