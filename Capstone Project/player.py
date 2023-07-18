#Author : Susindhar M	
#Date   : 17.07.2023
#Class-for-Capstone-Project

#importing libraries and class
from turtle import Turtle

class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.color("white")
		self.penup()
		self.goto(0,-240)
		self.setheading(90)
	
	#move turtle on keypress
	def move(self):
		self.fd(20)