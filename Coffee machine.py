#Author : Susindhar M
#Date   : 19.03.23
#Coffee-Machine-Proram

#User Setting inputs:
#Report
#Refill
#OFF

#Functions to be executed based on the type selected
def espresso(a):
	esp = [50,18,0]
	req = check_req(a,esp)
	if req!=1 :
		print(req)
	else:
		m=money(a[2],5)
		if m==1 :
			for i in range(0,3) : a[i]-=esp[i]
			print(f"Here is your {type}")
			a[3]+=5
		else :
			return

def latte(a):
	lat = [200,24,150]
	req = check_req(a,lat)
	if req!=1 :
		print(req)
	else:
		m=money(a[2],12)
		if m==1 :
			for i in range(0,3) : a[i]-=lat[i]
			print(f"Here is your {type}")
			a[3]+=12
		else :
			return

def cappuccino(a):
	cap = [250,24,100]
	req = check_req(a,cap)
	if req!=1 :
		print(req)
	else:
		m=money(a[2],18)
		if m==1 :
			for i in range(0,3) : a[i]-=cap[i]
			print(f"Here is your {type}")
			a[3]+=18
		else :
			return

#Function to check requirement for each type of coffee
def check_req(a,typ):
	req = ['water','milk','coffee']
	for i in range(1,3):
		if a[i]<typ[i]:
			return(f" Insufficient {req[i]}")
	else: return 1				
	
#Function for money input and calculation
def money(m,n):
	print(f"please insert {n} Rupees")
	total = int(input("How many Ones ?"))+int(input("How many twos ?"))*2+int(input("How many fives ?"))*5
	if total<5 :
		print("Money not enough")
		return 0
	else:
		change = total - n
		print(f"Here is your change {change}Rs")
		return 1		

#Function to refill the resourses	
def refill(a):
	a[0]+=300
	a[1]+=200
	a[2]+=200
	return 0

#Function to generate report on current resourses
def report(a):
	print(f"Water : {a[0]}ml")
	print(f"Milk : {a[1]}ml")
	print(f"Coffee : {a[2]}ml")
	print(f"Money : {a[3]}Rs")
	return 0

#Main Loop
sub_value = [0,0,0,0]
while 1:
	type = input("What would you like? (espresso/latte/cappuccino) : ").lower()
	if type == "off" : break
	try:
		exec(type+"(sub_value)")
	except NameError :
		print("Setting not available")

