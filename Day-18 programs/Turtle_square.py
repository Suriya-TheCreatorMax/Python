#Author : Susindhar M
#Date   : 10.07.2023
#Draw-square-using-Turtle

#Importing Library
from turtle import Turtle,Screen

#Initializing pointer
kenny = Turtle()
kenny.shape("turtle")

#Initializing Screen
screen = Screen()
screen.screensize(300,300)

#Drawing Square
kenny.forward(100)
kenny.right(90)
kenny.forward(100)
kenny.right(90)
kenny.forward(100)
kenny.right(90)
kenny.forward(100)
kenny.right(90)

#Wait for click to exit screen
screen.exitonclick()