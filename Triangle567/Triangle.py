# -*- coding: utf-8 -*-
"""
triangle.py

This module contains a function to classify triangles based on the lengths of their sides.
It checks if the given sides form a valid triangle and determines if the triangle is 
Equilateral, Isosceles, Right, or Scalene.

Created on Thu Jan 14 13:44:00 2016
Updated on Oct 30, 2024
"""

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.
    """
    # Check for invalid input
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        classification = 'InvalidInput'
    elif a > 200 or b > 200 or c > 200:
        classification = 'InvalidInput'
    elif a <= 0 or b <= 0 or c <= 0:
        classification = 'InvalidInput'
    # Check if it’s not a triangle
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        classification = 'NotATriangle'
    # Determine the type of triangle
    elif a == b == c:
        classification = 'Equilateral'
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        classification = 'Right'
    elif a == b or b == c or a == c:
        classification = 'Isosceles'
    else:
        classification = 'Scalene'
    return classification
