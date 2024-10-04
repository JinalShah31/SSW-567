# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

""" import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
 """

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Test for right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    # Test for equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')

    # Test for isosceles triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')
        self.assertEqual(classifyTriangle(7, 10, 7), 'Isosceles', '7,10,7 should be isosceles')
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isosceles', '6,6,4 should be isosceles')

    # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be scalene')
        self.assertEqual(classifyTriangle(7, 9, 10), 'Scalene', '7,9,10 should be scalene')

    # Test for invalid inputs
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is invalid')
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', '-1,2,3 is invalid')
        self.assertEqual(classifyTriangle(201, 199, 200), 'InvalidInput', '201,199,200 is invalid')
        self.assertEqual(classifyTriangle('a', 2, 3), 'InvalidInput', "'a',2,3 should be invalid input")
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', '1.5,2,3 should be invalid input')

    # Test for non-triangle cases
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should not form a triangle')
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 should not form a triangle')
        self.assertEqual(classifyTriangle(5, 9, 3), 'NotATriangle', '5,9,3 should not form a triangle')
        self.assertEqual(classifyTriangle(100, 50, 50), 'NotATriangle', '100,50,50 should not form a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

