#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: testMath
Author: Augustin Ward
Created: 2025-16-03
Version: 1.0
Description: Math between Grade 0-12 + College 1-4

License: NA
Contact: ward31513@gmail.com
Dependencies: mathInterface
"""

from mathInterface import *

'''
Types of Objects:
    |Numbers →      Numbers are objects that can go inside other objects listed
        Imaginary Numbers: i
        Real Numbers: Any
            [Irrational/Radical Numbers: sqrt(3), pi]
            [Rational Numbers: 1.2,3/4,-5/8 
             [Integers: -1,0,1 
              [Whole Numbers: 0,1,2 
               [Natural Numbers: 1,2,3]]]]
    |Points → 
        Array of points in a dictionary
        Single Point: Coordanite → (0,0)
        Two Points: Line → {(0,0), (1,1)}
        More Points on Same Plane: 2D Shape → {(0,0), (0,1), (1,0)}
        More Points in 3 Dimensions: 3D Shape → {(0,0,0), (1,0,0), (0,1,0), (0,0,1)}
    |Angles →
        Degrees
        Radians
        X & Y on Unit Circle
    |Matrix →
        Arrays in an Array or Dictionary
'''

"""
PEDMAS decides run order for Aritmethic, Measurment, Geometry, & Algebra

"""

def testArithmetic():
    # Operations: + - * /
    
    # Number Type: Natural, Integer, Fractions, Decimals, Percents
    
    # Properties: Cummutative, Associative, Distributive
    
    # Exponents: Powers, Roots
    
    # Order of Operations: PEDMAS
    
    pass

def testMeasurement():
    # Conversions: Length, area, volume, mass, time, temperature
    
    # Precision & Accuracy: Sig Figs, Error range
    
    # Guessing: Rounding, Estimation
    
    pass

def testGeometry():
    # Planes: Points, Lines, Angles
    
    # Shapes: Triangles, Squares, Polygons
    
    # Circles: Diameter, Radius, Circumference
    
    # 3D Shapes: Cubes, Cylinders, Pyramids...
    
    # Coordanite Plane: Distance, Midpoint, Slope
    
    # Transformations: Translations, Rotations, Relections, Dilations, Congruence, Similarity
    
    # Pythagorean Theorem
    
    pass
    
def testPreAlgebra():
    # Foundations: Factors, Multiples, Primes, Divisibility
    
    # Operations: Integers, Fractions, Decimals
    
    # Basics: Simple Expressions, Equations, Rations, Proportions
    
    pass

def testAlgebra():
    # Expresions: Simplification, Factoring, Polunomail Division
    
    # 2D Linear Equations
    
    # Systems of Equations
    
    # Quadratics: Quadratic Formula, Roots, Completing the Square
    
    # Exponents & Logarithms
    
    # Complex Numbers: Arithmetic, polar form
    
    # Sequences & Series: Summations
    
    pass

def testTrigonometry():
    # Functions: Sine, Cosine, Tangent, Secant, Cosecant, Cotangent
    
    # Angles: Degrees, Radians, Unit Circle
    
    # Graphs: Graphs, Shifts, Stretches, Reflections
    
    # Indentities: Pythagorean, Sum & Multiplication of Angles
    
    # Solving Trig Equations
    
    # Law of Sines, Law of Cosines
    
    # Usage to find missing sides/angles
    
    pass

def testPreCalculus():
    # Advanced Functions: Polynomial, Rational, Exponential, Logrithmic
    
    # Transformations: Shifts, Stretches, Parabolas, Hyperbolas
    
    # Advanced Summation and Patterns
    
    # Polar Coordanites, Parametric Equations
    
    # Intro to Limits: Inifinity
    
    # Intro to Vectors: Basic vectors and matrix
    
    pass

def testCalculus1():
    # Limits & Continuity
    
    # Tangent Lines & Rates of Change
    
    # Derivatives: Linearity, Product rule, Quotient rule, Chain rule
    
    # Advanced Derivatives: Trigonometric, Inverse, Implicit, Logarithmic
    
    # Applications: Related Rates, Max/Min, Curves
    
    # Fundamental Theorem of Calculus
    
    # Integration: u-substitution
    
    pass

def testCalculus2():
    # Advanced Integration: Integration by parts, partial fractions
    
    # Applications: Caclulating volume, arc lengths
    
    # Imporper Integrals
    
    # Sequences and Series: Convergence, power series, taylor series
            
    pass

def testCalculus3():
    # Vector Algebra: Coordinates & Vectors in 2D and 3D, dot & cross product, linear equations, polar/spherical coordinates
    
    # Vector Functions: Derivatives, Curvature
    
    # Several Variable Functions Limits, Continuity, Partial Derivatives, Linear approximations
    
    # Gradients & Directional Derivatives
    
    # Multiple Integrals: Double intergals over regions, including polar
    
    # Vector Fields, divergence, curl, surface integrals, Greens, Stokes, major theorems
    
    pass

def testMatrix():
    # Fundamentals: Matrix Def and Notations
    
    # Basic Operatuions, + - * scalar multiplaction, transpose
    
    # Determinants & Inverses
    
    # Solving: Gaussian elimination, cramers rule
    
    # Eignenvalues & vectors: Defs, Computation, Applications
    
    # Decomposition, Orthogonal matrices, symmetric matrices, + more
    
    pass

def testDiscrete():
    # Propositional and predicate logic
    
    # Sets, Venn Diagrams, Cardinality
    
    # Big O notation
    
    # Divisibility, div and mod, ceil, floor
    
    # Primes, factoring, lcm, gcd
    
    # Boolean Algebra: logic gates, truth tables 
    
    # Base conversion: between 10, 2, 8, 16
    pass


Testing = True
while (Testing == True):
    print("1. Arithmetic()  2. Measurement()  3. Geometry()")
    print("4. PreAlgebra()  5. Algebra()      6. Trigonometry()")
    print("7. Calculus1()   8. Calculus2()    9. Calculus3()")
    print("10. Matrix       11. Discrete      0. EXIT PROGRAM")
    testNum = int(input("Enter Test Number: "))
    
    if testNum == 0:
        Testing = False
    elif testNum == 1:
        testArithmetic()
    elif testNum == 2:
        testMeasurement()
    elif testNum == 3:
        testGeometry()
    elif testNum == 4:
        testPreAlgebra()
    elif testNum == 5:
        testAlgebra()
    elif testNum == 6:
        testTrigonometry()
    elif testNum == 7:
        testCalculus1()
    elif testNum == 8:
        testCalculus2()
    elif testNum == 9:
        testCalculus3()
    elif testNum == 10:
        testMatrix()
    elif testNum == 11:
        testDiscrete()
    else:
        pass
    print()
        
