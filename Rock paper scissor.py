#Author : Susindhar M
#Date   : 28.11.22
#Rock-Paper-Scissor

#library definition
import random

#Input
inp = int(input(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#Initializations
choice = ["Stone","Paper","Scissor"]
win = ["StonePaper","PaperScissor","ScissorStone"]
draw = ["StoneStone","PaperPaper","ScissorScissor"]
comp = random.choice(choice)
You = choice[inp]
out = comp + You

#Main Code
print(comp," ",You)
if out in win :
	print("You Win!")
elif out in draw :
	print("Its a draw")
else :
	print("You Lose :(")

