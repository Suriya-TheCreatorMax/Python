#Author : Susindhar M
#Date   : 26.12.22
#Basic-Calculator

#Decide First Number based on condition
def first_num(rep,res):
	if rep=='n':
		return int(input("Enter First Number :"))
	else :
		return res

#Calculate the result
def calculation(first,symbol,last):
	if symbol=='+':
		return first + last
	elif symbol=='-':
		return first - last
	elif symbol=='*':
		return first * last
	elif symbol=='/':
		return first / last

#Initialization
repeat = 'n'
result = 0

#Main loop	
while repeat!='x':
	operand_1 = first_num(repeat,result)
	operator = input("+\n-\n*\n/\nPick an operator :")
	operand_2 = int(input("Enter Second Number :"))
	result = calculation(operand_1,operator,operand_2)
	print(operand_1,operator,operand_2,"=",result)
	repeat = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation or type 'x' to exit :")
