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
	str_index = random.randint(0,51)
	password+=letter[str_index]

#Generating random number
for i in range(0,number_input):
	str_index = random.randint(0,9)
	password+=number[str_index]

#Genenrating random
for i in range(0,symbol_input):
	str_index = random.randint(0,13)
	password+=symbol[str_index]

#Shuffling the password
pass_len = letter_input + number_input + symbol_input
for i in range(0,pass_len-1):
	temp_list.append(i)
random.shuffle(temp_list)
for i in range(0,pass_len-1):
	pswd+=password[temp_list[i]]

	

#Printing the output
print(pswd)



