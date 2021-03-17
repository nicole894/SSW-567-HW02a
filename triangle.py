# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(_a, _b, _c):
    """
    Your correct code goes here...Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if _a > 200 or _b > 200 or _c > 200:
        return 'InvalidInput'

    if _a <= 0 or _b <= 0 or _c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(_a, int) and isinstance(_b, int) and isinstance(_c, int)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (_a > (_b + _c)) or (_b > (_a + _c)) or (_c > (_a + _b)):
        return 'NotATriangle'

    # Right angled
    sides = [_a, _b, _c]
    sides.sort()
    if sides[2] ** 2 == ((sides[0] ** 2) + (sides[1] ** 2)):
        return 'Right'

    # now we know that we have a valid triangle
    if _a == _b and _b == _c:
        return 'Equilateral'

    if (_a != _b) and (_b != _c) and (_a != _c):
        return 'Scalene'

    return 'Isosceles'
