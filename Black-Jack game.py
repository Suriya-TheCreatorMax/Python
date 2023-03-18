#Author : Susindhar M
#Date   : 18.03.2023
#The - BlackJack - Game

#Importing libraries
import random

#Function to pick a random card
def pickCard():
	cardList = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	pick = random.randint(0,12)
	return cardList[pick]

#Dealer's play Function
def dealerEndScore():
	if sum(dealerCard)<=17:
		dealerCard.append(pickCard())
	return sum(dealerCard)

#Player's Score Function
def playerEndScore():
	if hit_pass == 'y':
		playerCard.append(pickCard())
	return sum(playerCard)

#Result Deciding Function
def gameDecision():
	if dealerScore>21 and playerScore>21:	
		return "Draw"
	elif dealerScore>21 and playerScore<21:
		return "You Win"
	elif dealerScore<=21 and playerScore<=21:
		if playerScore>dealerScore:
			return "You Win"
		elif playerScore==dealerScore:
			return "Draw"
		else:
			return "You Lose"
	else:
		return "You Lose"

#Distributing cards for player and dealer
playerCard = [pickCard(),pickCard()]
dealerCard = [pickCard(),pickCard()]


#Main Function
print("Your Cards :",playerCard,"Your Score :",sum(playerCard))
print("Computer's First Card :",dealerCard[0])
hit_pass = input("press 'y' to hit / press 'n' to pass : ")
dealerScore = dealerEndScore()
playerScore = playerEndScore()
result = gameDecision()

#Output Presentation
print("Your final Hand :",playerCard,"Final Score :",playerScore)
print("Computer's final Hand :",dealerCard,"Final Score :",dealerScore)
print(result)

