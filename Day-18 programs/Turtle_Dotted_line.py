#Author : Susindhar M
#Date   : 10.07.2023
#Draw-Dotted-line

#Importing Library
from turtle import Turtle,Screen

#Initializing pointer
kenny = Turtle()
kenny.shape("turtle")

#Initializing Screen
screen = Screen()
screen.screensize(300,300)

#Drawing dotted_line
for i in range(0,100):
	kenny.forward(2)
	kenny.up()
	kenny.forward(2)
	kenny.down()

#Wait for click to exit screen
screen.exitonclick()