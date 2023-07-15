#Author : Susindhar M
#Date   : 15.07.2023
#Class-for-paddle-game

#importing libraries and classes
from turtle import Turtle

class Pads(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.penup()
		self.shapesize(stretch_wid=0.6,stretch_len=3.7)
		self.color("white")
		self.setheading(90)

	#Functions for movement of pad
	def up(self):
		if self.pos()[1]<280 : self.fd(20)
		
	def down(self):
		if self.pos()[1]>-280 : self.bk(20)