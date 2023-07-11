#Author : Susindhar M
#Date   : 11.07.2023
#Hirst-Painting-Program

#importing libraries
import colorgram
from random import choice
import turtle

#Function to convert colorgram output to tuple format
def generate_color(color):
	r = color.r
	g = color.g
	b = color.b
	return (r,g,b)

#Importing image colors
turtle.colormode(255)
colors = colorgram.extract("hirst_painting.jpeg",100)
rgb_colors = []
for color in colors:
	rgb_tuple = generate_color(color.rgb)
	rgb_colors.append(rgb_tuple)

#Instances creation and setup
kenny = turtle.Turtle()
kenny.hideturtle()
white_screen = turtle.Screen()
kenny.up()
white_screen.screensize(2000,1500)

#Main Loop
for i in range(0,100):
	col = choice(rgb_colors)
	if (i/10)%2==0 and i!=0 :
		kenny.left(90)
		kenny.fd(50)
		kenny.dot(20, col)
		kenny.left(90) 
		
	elif (i/10)%2==1 :
		kenny.right(90)
		kenny.fd(50)
		kenny.dot(20, col)
		kenny.right(90) 
		
	else:
		kenny.fd(50) 
		kenny.dot(20, col)

#Screen Termination on click
white_screen.exitonclick()
