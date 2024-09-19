
import unittest
import math
from classifyTriangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
    
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
    
    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
    
    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles and Right")
    
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a triangle")
    
    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not a triangle")
    
if __name__ == '__main__':
    unittest.main()
