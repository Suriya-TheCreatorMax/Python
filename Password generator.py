#Author : Susindhar M
#Date   : 28.11.22
#Python password Generaor

#Library file
import random

#Title
print("Python password Generator\n")

#Initializations
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "!@#$%^&*()_-+="
password = ""
pswd = ""
temp_list = []


#Inputs
letter_input = int(input("No. of letters needed : "))
number_input = int(input("No. of numbers needed : "))
symbol_input = int(input("No. of symbols needed : "))

#Main code
#Generating random letter
for i in range(0,letter_input):
	password+=random.choice(letter)
	
#Generating random number
for i in range(0,number_input):
	password  += random.choice(number)
	
#Genenrating random
for i in range(0,symbol_input):
	password += random.choice(symbol)
	

#Shuffling the password
pass_len = letter_input + number_input + symbol_input
for i in range(0,pass_len):
	temp_list.append(i)
random.shuffle(temp_list)
for i in temp_list:
	pswd+=password[i]
	

#Printing the output
print(pswd)



