#Author : Susindhar M
#Date   : 18.03.23
#Number-Guessing-Game

#Importing Library
import random as r

#Introduction presentation
print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

#Difficulty Selection
difficulty = input("Easy or Hard :") 
if difficulty == "Easy":
	attempt = 10
else:
	attempt = 5

#Main Program
number = r.randint(0,100)
loop = attempt

while loop!=0:
	print(f"You have {loop} attempts remaining to guess the number.")
	guess = int(input("Make a Guess : "))
	if guess>number :
		print("Too High\nGuess again")
	elif guess<number :
		print("Too Low\nGuess again")
	else :
		print("You Win")
		break
	loop-=1

if loop==0:
	print("You Lose")
