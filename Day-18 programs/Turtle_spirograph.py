#Author : Susindhar M
#Date   : 10.07.2023
#Random-Walk

#Importing Library
import turtle
import random

#Generate random color
turtle.colormode(255)
def generate_color():
	r = random.randint(0, 255)	
	g = random.randint(0, 255)
	b = random.randint(0, 255) 
	return (r,g,b)	

#Initializing pointer
kenny = turtle.Turtle()
kenny.shape("turtle")
kenny.speed(100) #increased speed

#Initializing Screen
screen = turtle.Screen()
screen.screensize(300,300)

#Creating spirograph
for i in range(0,180):
	kenny.pencolor(generate_color())
	kenny.circle(100)
	kenny.right(2)

#Wait for click to exit screen
screen.exitonclick()