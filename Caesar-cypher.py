#Author : Susindhar M
#Date   : 09-12-2022
#Caesar-Cypher

#Initializing global variable
alphabet_NC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Encode function definition
def encode():

	#Variable initializations
	e_code=""
	alphabet = alphabet_NC.copy()
	message = input("\nEnter your Message Here :").lower()
	key = int(input("Enter the number of shifts : "))

	#Shifted alphabet list generation
	for j in range (0,key):
		for i in range (0,25):
			temp = alphabet[i]
			alphabet[i] = alphabet[i+1]
			alphabet[i+1] = temp

	#code word generation
	for i in range(0,len(message)):
		for j in range(0,25):
			if alphabet_NC[j]==message[i]:
				e_code+=alphabet[j]
	
	#Printing out result
	print(e_code)

#decode function definition
def decode():

	#variable initialization
	d_code=""
	alphabet = alphabet_NC.copy()
	message = input("\nEnter your Message Here :").lower()
	key = int(input("Enter the number of shifts : "))
	
	#Shifted alphabet list generation
	for j in range (0,key):
		for i in range (25,0,-1):
			temp = alphabet[i-1]
			alphabet[i-1] = alphabet[i]
			alphabet[i] = temp

	#code word generation
	for i in range(0,len(message)):
		for j in range(0,25):
			if alphabet_NC[j]==message[i]:
				d_code+=alphabet[j]
	
	#Printing out result
	print(d_code)

#Main Code			
print("\nWelcome to caesar Cypher!\n")

#Main Loop
while True:			
	func = input("Type 'Encode' to encrypt or 'decode' to decrypt : ").lower()
	#Function selection
	if func=="encode":
		encode()
	elif func=="decode":
		decode()
	else:
		print("Not Valid :(")

	cont = input("Type 'Yes' to Continue or 'No' to Exit : ").lower()	
	#Loop decision
	if cont=="no":
		break
	
	
	