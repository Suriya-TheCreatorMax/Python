#Author : Susindhar M	
#Date   : 17.07.2023
#Capstone-Project

#importing libraries and class
from turtle import Screen
from cars import Cars
from level import Level
from player import Player
import time
import random

#Playground setup
playground = Screen()
playground.setup(500, 500)
playground.bgcolor("black")
playground.title("Capstone")
playground.tracer(0)

#Creating object instances
crosser = Player()
score = Level()
car_obj = Cars()

#Listening for key press
playground.listen()
playground.onkeypress(crosser.move,"Up")

#Main loop
game_on=1
while game_on:
	
	#change level speed
	time.sleep(0.1/score.lev)
	
	#creating cars	
	car_obj.spawn()
	car_obj.move()
	
	#Detect collision with car
	for car in car_obj.all_cars:
		if car.distance(crosser)<20:
			score.Gameover()
			game_on=0

	#Detect level pass
	if crosser.ycor()>240:
		crosser.goto(0,-240)
		score.displev()
	
	playground.update()


#Exit on click
playground.exitonclick()