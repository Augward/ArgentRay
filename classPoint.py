#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: classPoint
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0
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
    def __init__(self, point):
        self.point = point