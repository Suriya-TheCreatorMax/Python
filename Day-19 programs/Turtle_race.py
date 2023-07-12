#Author : Susindhar M
#Date   : 11.07.2023
#Turtle_Race_application

#importing libraries
import turtle
import random

#Global variable declaration
colors = ["red", "green" ,"blue" ,"orange" ,"purple"]
y_coor = [0, 90, -90, 180, -170]
objs = []
win = "?"

#Creating Screen class instance and setup
playground = turtle.Screen()
playground.setup(400, 400)
playground.title("Turtle Championship")

#Function to enable user to place bet
def place_bet():
	inp = playground.textinput("Bet Zone","Which color turtle you want to bet on :")
	return inp

#check coordinates of every turtle(To determine end of race)
def check_coor():
	for tur in objs:
		x_pos = tur.position()
		if x_pos[0]>160 : 
			global win
			win = tur.color()[1]
			print(win)
			return 0
	return 1

#Function to declare the winner
def winner():
	print(win)
	if win in user_1:
		print("Player_1 Wins")
	elif win in user_2:
		print("Player_2 Wins")
	else : print("You guys suck")

#Creating turtle class instance and setup
for tur in range(0,5):
	kenny = turtle.Turtle(shape = "turtle")
	kenny.color(colors[tur])
	kenny.penup()
	kenny.goto(-180,y_coor[tur])
	objs.append(kenny)

#place user bets
user_1 = place_bet()
user_2 = place_bet()

#main loop
while check_coor():
	for tur in objs:
		tur.fd(random.randint(0,5))
winner()

#Exit the screen on click
playground.exitonclick()