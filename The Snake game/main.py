#Author : Susindhar M
#Date   : 12.07.2023
#The-Snake-Game

#importing libraries
from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time

#Setting up background
playground = Screen()
playground.bgcolor("black")
playground.setup(600, 600)
playground.title("Nokia Snake Game")
playground.tracer(0)

#Creating snake, food and score instances
snak_food = Food()
points = Score()
player = Snake()

#Listen to the key press
playground.update()
playground.listen()
playground.onkey(player.up,"Up")
playground.onkey(player.down,"Down")
playground.onkey(player.left,"Left")
playground.onkey(player.right,"Right")

#Function for tail collision
def tail_collision():
	for part in player.snake:
		if part == player.snake[1] or part == player.snake[2] : continue
		elif player.snake[1].distance(part)<10: 
			points.game_over()
			return 1
	return 0

#Main loop
while 1: 
	
	#Continuous movement of snake
	time.sleep(0.1)
	player.move()
	
	#Detecting food collision
	if player.snake[0].distance(snak_food)<15:
		snak_food.refresh()
		points.add_score()
		player.extend()

	#Detecting wall collision
	if abs(player.snake[0].xcor())>270 or abs(player.snake[0].ycor())>270:
		points.game_over()
		playground.update()
		break
	
	#Detecting tail collision
	if tail_collision(): break
	
	#Update screen	
	playground.update()	

#Exit playground on click
playground.exitonclick()