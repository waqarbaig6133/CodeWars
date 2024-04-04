'''
Based on the received dimensions, a and b, of an ellipse, calculare its area and perimeter.
ex)
Input: ellipse(5,2)

Output: "Area: 31.4, perimeter: 23.1"

'''

from math import pi
from math import sqrt
def ellipse(a, b):
    return "Area: " + str(round(pi*a*b, 1)) + ", perimeter: " + str(round(pi*((3/2*(a+b) - sqrt(a*b))),1)) 
