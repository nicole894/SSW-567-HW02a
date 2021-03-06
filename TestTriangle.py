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

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(4, 7, 5), 'Scalene', '4,7,5 should be scalene')

    def testInvalidTriangles(self):
        self.assertEqual(classify_triangle(3, 3, 15), 'NotATriangle', '3,3,15 is not a triangle')

    def testOutUpperBoundTriangles(self):
        self.assertEqual(classify_triangle(344, 300, 199), 'InvalidInput', 'data is outside upper bound')

    def testOutLowerBoundTriangles(self):
        self.assertEqual(classify_triangle(0, -1, 2), 'InvalidInput', 'data is outside lower bound')


    def testInvalidDataTriangles(self):
        with self.assertRaises(TypeError):
            self.assertEqual(classify_triangle('x', 'y', 'z'), 'InvalidInput', 'x,y,z is not valid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

