import random
inp = int(input(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choice = ["Stone","Paper","Scissors"]
win = ["StonePaper","PaperScissor","ScissorsStone"]
draw = ["StoneStone","PaperPaper","ScissorsScissors"]
comp = random.choice(choice)
You = choice[inp]
out = comp + You
print(comp," ",You)
if out==win[0] or out==win[1] or out==win[2] :
	print("You Win!")
elif out==draw[0] or out==draw[1] or out==draw[2] :
	print("Its a draw")
else :
	print("You Lose :(")

