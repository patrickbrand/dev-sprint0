# Polygon excercise from Week 0

# Name: Patrick Brand

import math
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def polygon(turtle, length, n):
    for i in range(int(n)):
        angle = 360 / n
        fd(turtle, length)
        lt(turtle, angle)
        
# polygon(bob, 100, 6)

def circle(turtle, r):
    circumference = math.pi * (2 * r)
    print 'circumference is ' + str(circumference)
    polygon(turtle, 10, circumference)
    
# circle(bob, 5)

def arc(turtle, r, theta):
# circumference = math.pi * (2 * r)
    length = 1
    for i in range(int(theta)):
        angle = 360 / theta
        fd(turtle, length)
        lt(turtle, angle)

arc(bob, 5, 360)

wait_for_user()					
