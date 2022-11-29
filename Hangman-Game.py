#Author : Susindhar M
#Date   : 29.11.22
#The-Hangman-Game

#Importing libraries
import random


# Image Initializations 
disp_list =["  +-----+\n  |     |\n  |     |\n  O     |\n /|\    |\n / \    |\n        |\n        |\n________|_______",
            "  +-----+\n  |     |\n  |     |\n  O     |\n /|\    |\n        |\n        |\n        |\n________|_______",
		"  +-----+\n  |     |\n  |     |\n  O     |\n  |     |\n        |\n        |\n        |\n________|_______",
		"  +-----+\n  |     |\n  |     |\n  O     |\n        |\n        |\n        |\n        |\n________|_______",
		"  +-----+\n  |     |\n  |     |\n        |\n        |\n        |\n        |\n        |\n________|_______",]


#Variable Initializations
lives = 4		
blank_check = 0
answer_list = []

#Choose a random word
Question_list = ["apple","orange","banana"]
Question_word = Question_list[random.randint(0,len(Question_list)-1)]

#Empty dash list
for i in range(0,len(Question_word)):
	answer_list.append("_")

#Main loop
while blank_check != len(Question_word) and lives!=0 :
	lives_check = blank_check
	blank_check = 0
	guess = input("Guess a letter : ").lower() 
	
	#check if the guessed letter is in word
	for str_index in range(0,len(Question_word)): 
		if guess==Question_word[str_index]:
			answer_list[str_index] = guess
		
	#Check the number of blanks remaining
	for str_index in range(0,len(Question_word)): 
		if answer_list[str_index] != '_' :
			blank_check+=1

	#No. of lives remaining calculation
	if lives_check == blank_check:
		lives-=1
	
	#Display progress content	
	print(disp_list[lives])
	for i in answer_list:
		print(i)

#Display final input
if lives>0:
	print("You Win!")
else :
	print("You lose :(")
		
	
		
		
	