#Author : Susindhar M
#Date   : 15.07.2023
#Class-for-paddle-game

#importing libraries and classes
from turtle import Turtle

class Score(Turtle):
	def __init__(self,x):
		super().__init__()
		self.x=x
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(self.x,280)
		self.score = 0
		self.write(self.score, move=False, align='left', font=('Arial', 14, 'bold'))
	
	#Function to add score
	def scoreadd(self):
		self.score+=1
		self.clear()
		self.write(self.score, move=False, align='left', font=('Arial', 14, 'bold'))

	