"""Heber Portal Reyes CS 100 2021F Section 199 HW 03, September 26, 2021"""

import turtle
s = turtle.Screen()
worm = turtle.Turtle()

worm.forward (100)
worm.left (120)
worm.forward (100)
worm.left (120)
worm.forward (100)
worm.left (90)

worm.goto(-120,100)
worm.forward (100)
worm.left (90)
worm.forward (100)
worm.left (90)
worm.forward (100)
worm.left (90)
worm.forward (100)

worm.goto(-250,250)
worm.forward (100)
worm.left (72)
worm.forward (100)
worm.left (72)
worm.forward (100)
worm.left (72)
worm.forward (100)
worm.left (72)
worm.forward (100)
worm.left (72)


for i in range(1, 100, 20):
    worm.right(90)   
    worm.forward(i)   
    worm.right(270)   
    worm.pendown()    
    worm.circle(i)    
    worm.penup()      
    worm.home()

import math
num = 100
print ("The factorial of 100 is - ")
print(math.factorial(int(num)))

print ("The log base 2 of 1,000,000 - ")
a = (1000000)
Base = (2)
print (math.log(a,Base))

print ("The GCD of 63 and 49 is - ")
math.gcd(63,49)
print (math.gcd(63,49))







