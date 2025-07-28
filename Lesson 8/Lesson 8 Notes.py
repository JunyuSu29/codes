'''
Functions
A function is a block of code that only runs when it is called.
It takes in inputs, called parameters, and runs the function to create an output. 
Function structure: def function_name(parameters):
    Code to execute
    return output
'''
#For example:
import math

def distance(pt1,pt2):
    x1,y1=pt1
    x2,y2=pt2
    return math.sqrt(math.pow(x2-x1),2)+math.pow(y2-y1,2)
#This example returns the distance between two points in a 2D Cartesian Plane. 
