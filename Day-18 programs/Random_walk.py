#Author : Susindhar M
#Date   : 10.07.2023
#Random-Walk

#Importing Library
from turtle import Turtle,Screen
import random

#Initializing pointer
kenny = Turtle()
kenny.shape("turtle")
kenny.pensize(10) #increased thickness
kenny.speed(9) #increased speed

#Initializing Screen
screen = Screen()
screen.screensize(300,300)

#Making a rangom walk
for i in range(0,100):
	move = random.randint(1,4)
	if move==1: 
		kenny.pencolor("red")
		kenny.forward(20)
	elif move==2: 
		kenny.pencolor("blue")
		kenny.backward(20)
	elif move==3: 
		kenny.pencolor("yellow")
		kenny.right(90)
		kenny.forward(20)
	elif move==4: 
		kenny.pencolor("green")
		kenny.left(90)
		kenny.forward(20)

#Wait for click to exit screen
screen.exitonclick()