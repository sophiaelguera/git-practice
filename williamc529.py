# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming
# Not written by William
# Citation: https://www.geeksforgeeks.org/turtle-programming-python/

import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.exitonclick()

# It draws spiral helix that's kinda cool lol

