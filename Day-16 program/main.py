#Author : Susindhar M
#Date   : 05.07.2023
#Cofee_Machine_Program_OOPS

#Importing classes from local folder
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Object instances
inventory=Menu()
cafeMachine = CoffeeMaker()
cashier = MoneyMachine()

#Main loop
while 1:	
	type = input("What would you like? (espresso/latte/cappuccino) : ").lower()
	if type == "off" : break
	elif type == "report" : 
		cafeMachine.report()
		cashier.report()
		continue
	else:
		drink = inventory.find_drink(type)
		if drink is None : continue
		if cafeMachine.is_resource_sufficient(drink):
			if cashier.make_payment(drink.cost) :
				cafeMachine.make_coffee(drink)
		
		
				
