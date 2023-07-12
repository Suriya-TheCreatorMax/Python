#Author : Susindhar M
#Date   : 11.07.2023
#Sketch_app

#importing libraries
import turtle

#Creating Instances
pencil = turtle.Turtle()
sketch = turtle.Screen()
pencil.speed("fastest")

#Functions for pointer movement
def front():
	pencil.fd(30)

def back():
	pencil.bk(30)

def clock():
	pencil.left(10)

def a_clock():
	pencil.right(10)

def clean():
	pencil.clear()

#Take user input
sketch.listen()
sketch.onkeypress(front, "Up")
sketch.onkeypress(back, "Down")
sketch.onkeypress(clock, "Left")
sketch.onkeypress(a_clock, "Right")
sketch.onkeypress(clean, "c")

#Terminate screen on click
sketch.exitonclick()
