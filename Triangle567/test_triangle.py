# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    # Test for Right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    # Test for Equilateral triangles    
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classify_triangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')

    # Test for isosceles triangles
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')
    def testIsoscelesTrianglesB(self):
        self.assertEqual(classify_triangle(7, 10, 7), 'Isosceles', '7,10,7 should be isosceles')
        
    # Test for scalene triangles
    def testScaleneTrianglesA(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '3,4,6 should be scalene')
    
    def testScaleneTrianglesB(self):
        self.assertEqual(classify_triangle(7, 9, 10), 'Scalene', '7,9,10 should be scalene')

    # Test for invalid inputs
    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 is invalid')
    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'InvalidInput', '-1,2,3 is invalid')
    def testInvalidInputC(self):
        self.assertEqual(classify_triangle('a', 2, 3), 'InvalidInput', "'a',2,3 should be invalid input")
       

    # Test for non-triangle cases
    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle', '1,2,3 should not form a triangle')
    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(10, 1, 1), 'NotATriangle', '10,1,1 should not form a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

