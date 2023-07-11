#Author : Susindhar M
#Date   : 10.07.2023
#Draw-Polygons

#Importing Library
from turtle import Turtle,Screen

#Initializing pointer
kenny = Turtle()
kenny.shape("turtle")

#Initializing Screen
screen = Screen()
screen.screensize(300,300)

#Drawing Polygons
for i in range(3,11):
	angle = 360/i
	for j in range(0,i):
		kenny.forward(100)
		kenny.right(angle)	

#Wait for click to exit screen
screen.exitonclick()