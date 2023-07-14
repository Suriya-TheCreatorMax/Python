#Author : Susindhar M
#Date   : 12.07.2023
#Class-for-The-Snake-Game

#importing libraries
from turtle import Turtle
from random import randint

class Food(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.up()
		self.shapesize(stretch_len=0.5,stretch_wid=0.5)
		self.color("blue")
		self.speed(10)
		self.refresh()
	
	#Relocate the food
	def refresh(self):
		self.goto(randint(-290,290),randint(-290,290))