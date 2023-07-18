#Author : Susindhar M	
#Date   : 17.07.2023
#Class-for-Capstone-Project

#importing libraries and class
from turtle import Turtle
import random
import time

class Cars:
	def __init__(self):
		self.all_cars=[]		
	
	#move the cars forward
	def move(self):
		for car in self.all_cars:
			car.fd(20)
	
	#create cars
	def spawn(self):
		if random.randint(1,6)==1:
			new_car=Turtle()		
			new_car.shape("square")
			new_car.color("white")
			new_car.penup()
			new_car.setheading(180)
			new_car.shapesize(stretch_wid=1, stretch_len=2)
			new_car.goto(random.randint(240,300),random.randint(-200,220))
			self.all_cars.append(new_car)
		
		
