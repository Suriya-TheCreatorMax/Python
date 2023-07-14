#Author : Susindhar M
#Date   : 12.07.2023
#Class-for-The-Snake-Game

#importing libraries
from turtle import Turtle,Screen

#class creation
class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.cur_score = 0
		self.pencolor("white")
		self.ht()
		self.up()
		self.goto(0,280)
		self.write(f"Score = {self.cur_score}", align="center", font=('Arial', 14, 'normal'))
	
	#Prints game over in the game screen
	def game_over(self):
		self.goto(0, 0)
		self.write(f"Game Over", align="center", font=('Arial', 14, 'normal'))
	
	#Display score on the screen		
	def add_score(self):
		self.clear()
		self.cur_score+=1 
		self.write(f"Score = {self.cur_score}", align="center", font=('Arial', 14, 'normal'))

