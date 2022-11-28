print("Welcome to the decision making game")
path = input("There are two paths which path would you like to go? (Left/Right) : ")
if path=="Left":
	lake = input("You have a lake in front of you would you swim or wait for boat? (Swim/Wait) :")
	if lake=="Wait":
		door = input("There are three doors in front of you choose one (Red/Yellow/Blue) :")
		if door=="Red":
			print("You win!")
		else :
			print("Game Over")
	else :
		print("Game Over")
else :
	print("Game Over")