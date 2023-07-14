#Author : Susindhar M
#Date   : 12.07.2023
#Class-for-The-Snake-Game

#importing libraries
from turtle import Turtle
import time

#Class content
class Snake:
	def __init__(self):
		self.snake = []
		for i in range(0,4):
			self.add_tail(-20*i,0)
			
	#Add segments to snake body
	def add_tail(self, posx,posy):
		self.body = Turtle(shape = "square")
		self.body.up()
		self.body.color('white')
		self.body.goto(posx,posy)
		self.body.speed(10)
		self.snake.append(self.body)

	#provide coordinates for add_tail function
	def extend(self):
		x = self.snake[-1].xcor()
		y = self.snake[-1].ycor()
		self.add_tail(x,y)
			
	
	#Function that defines the movement of the snake
	def move(self):
		for i in range(len(self.snake)-1,-1,-1):
			if i==0:
				self.snake[i].fd(20)		
			else:
				self.snake[i].goto(self.snake[i-1].position())
	
	#Function that defines the upward movement of the snake
	def up(self):
		dir = self.snake[0].heading()
		if  dir in [90, 270] : return 0
		for i in range(len(self.snake)-1,-1,-1):
			if i==0:
				if dir == 0 : self.snake[i].left(90)	
				else : self.snake[i].right(90)
			else:
				self.snake[i].goto(self.snake[i-1].position())

	#Function that defines the downward movement of the snake
	def down(self):
		dir = self.snake[0].heading()
		if dir in [90, 270] : return 0
		for i in range(len(self.snake)-1,-1,-1):
			if i==0:
				if dir == 0 : self.snake[i].right(90)	
				else : self.snake[i].left(90)
			else:
				self.snake[i].goto(self.snake[i-1].position())

	#Function that defines the leftward movement of the snake
	def left(self):
		dir = self.snake[0].heading()
		if dir in [0, 180] : return 0
		for i in range(len(self.snake)-1,-1,-1):
			if i==0:
				if dir == 90 : self.snake[i].left(90)	
				else : self.snake[i].right(90)		
			else:
				self.snake[i].goto(self.snake[i-1].position())

	#Function that defines the rightward movement of the snake
	def right(self):
		dir = self.snake[0].heading()
		if dir in [0, 180] : return 0
		for i in range(len(self.snake)-1,-1,-1):
			if i==0:
				if dir == 90 : self.snake[i].right(90)	
				else : self.snake[i].left(90)	
			else:
				self.snake[i].goto(self.snake[i-1].position())

	