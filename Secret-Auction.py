#Author : Susindhar M
#Date   : 26.12.22
#Secret-Auction

#Importing libraries
from os import system

#Function to find the highest bid's name
def find_greater():
	high = 0
	for name in bid:
		if(high<bid[name]):
			winner = name
	return winner

#Clear screen
system('cls')

#Initializations
bid = {}
isRepeat="yes"


#Main Loop
while isRepeat=="yes":
	print("Welcome to Secret Auction\n")

	#Getting Inputs from user
	name = input("Type your name :")
	bid[name] = int(input("Enter the value of your bid : $"))
	isRepeat = input("Is there another bidder (yes/no) :")

	#clear screen
	system('cls')

#Function call
result=find_greater()

#Final Output
print("The winner is ",result,"with a bid of $",bid[result] )