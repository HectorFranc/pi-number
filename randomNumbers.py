# Having a circle inscribed in a square, pi is 4 times circle area divided by square area.
# For know circle and square areas we will use random numbers, for x and y position of 'n' points in the square but maybe not in the circle.
# The area of the square/circle will be the number of points that are in the square/circle.
# Our square will be at points: (0, 0), (0, 1), (1, 1), (1, 0), its slide is 1, and circle radius too.
from math import sqrt, pi
from random import random

def isInCircle(x, y):
    distanceFromCenter = sqrt((x-0.5)**2 + (y-0.5)**2)
    return distanceFromCenter <= 0.5

def randomNumbersMethod(n=10):
    squareArea = 0
    circleArea = 0
    for k in range(n):
        # Set x and y random positions
        xRandom = random()
        yRandom = random()
        # Everytime the point is in the square because 0 <= x < 1 and 0 <= y < 1
        squareArea += 1
        # If point is in circle, add 1 to circle area
        if isInCircle(xRandom, yRandom):
            circleArea += 1
    # "pi is 4 times circle area divided by square area"
    pi_value = 4*circleArea/squareArea

    print(f'The pi value is: {pi_value}\nThe diference is:{pi-pi_value}')
    return pi_value

randomNumbersMethod(100000)
