#Author : Susindhar M
#Date   : 15.07.2023
#Class-for-paddle-game

#importing libraries and classes
from turtle import Turtle
import random as r

class ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.speed(1)
		self.penup()
		self.x = 10
		self.y = 10

	#Function for motion of ball
	def move(self):
		self.goto(self.xcor()+self.x,self.ycor()+self.y)

	#Function to bounce ball at top and bottom wall		
	def bounce_wall(self):
		self.y *= -1

	#Function to bounce ball at pad
	def bounce(self):
		self.x *= -1


	