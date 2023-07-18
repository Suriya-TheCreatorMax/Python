#Author : Susindhar M	
#Date   : 17.07.2023
#Class-for-Capstone-Project

#importing libraries and class
from turtle import Turtle

class Level(Turtle):
	def __init__(self):
		super().__init__()
		self.ht()
		self.penup()
		self.color("white")
		self.goto(-230,230)
		self.lev=0
		self.displev()

	#Increament and display level
	def displev(self):
		self.lev+=1
		self.clear()
		self.write(f"Level : {self.lev-1}", font=('Arial', 14, 'normal'))

	#Triggers on game over
	def Gameover(self):
		self.goto(-30,0)
		self.write("GAME OVER !", font=('Arial', 14, 'normal'))