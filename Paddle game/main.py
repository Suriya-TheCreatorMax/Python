#Author : Susindhar M
#Date   : 15.07.2023
#Paddle-game

#importing libraries and classes
from turtle import Screen, Turtle
from pads import Pads
from Ball import ball
from score import Score
import time

#Setting Initial status of screen
playground = Screen()
playground.setup(600,600)
playground.tracer(0)
playground.title("Paddle Game")
playground.bgcolor("black")
player_1 = Pads()
player_1.goto(-280,0)
player_2 = Pads()
player_2.goto(280,0)
dot = ball()
point_1 = Score(-50)
point_2 = Score(50)

#Function for exit
def exit():
	global not_exit
	not_exit=0

#Seperate player fields
line = Turtle()
line.ht()
line.color("white")
line.up()
line.goto(0,300)
line.setheading(270)
for i in range(0,70):
	line.down()
	line.fd(10)
	line.up()
	line.fd(10)

#Controlling the pads
playground.listen()
playground.onkeypress(player_1.up,"w")
playground.onkeypress(player_1.down,"s")
playground.onkeypress(player_2.up,"Up")
playground.onkeypress(player_2.down,"Down")
playground.onkey(pause,"p")
playground.onkey(exit,"x")

#Main loop
not_exit=1
while not_exit: 
	time.sleep(0.07)
	playground.update()	
	dot.move()
	x = dot.xcor()
	y = dot.ycor()

	#Detecting wall collision
	if abs(y)>280 : dot.bounce_wall()

	#Detecting pad collision
	elif (dot.distance(player_1)<50 or dot.distance(player_2)<50) and abs(x)>265 : 
		dot.bounce() 
		if dot.speed()<10 : dot.speed(dot.speed()+1)
	
	#Detecting pad miss	
	elif abs(x)>275 : 
		dot.goto(0,0)
		dot.bounce()
		if x>0 : point_1.scoreadd()
		else : point_2.scoreadd()
	
		

#Exit on click
playground.exitonclick()