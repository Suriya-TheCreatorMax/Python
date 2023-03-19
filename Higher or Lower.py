#Author : Susindhar M
#Date   : 19.03.23
#Higher-or-Lower

#Game Rules :
#	*Guess who has more instagram followers among 2 people.
#	*The game continues until you get the answer wrong.

#Game Data (Should not be Modified inside program)
DATA = [{'name':"RDJ",
	   'job':"Film Actor",
	   'from':"an American",
	   'follow':55.1},

	  {'name':"Tom Cruise",
	   'job':"Film Actor",
	   'from':"an American",
	   'follow':9},	 

	  {'name':"M S Dhoni",
	   'job':"Cricket player",
	   'from':"an Indian",
	   'follow':40.8},

	  {'name':"Zendaya",
	   'job':"Actress",
	   'from':"an American",
	   'follow':171},

	  {'name':"Mia Khalifa",
	   'job':"Porn Actress",
	   'from':"a Labanese",
	   'follow':25.2},

	  {'name':"Messi",
	   'job':"Football player",
	   'from':"a Paris",
	   'follow':442},

	  {'name':"Ronaldo",
	   'job':"Football player",
	   'from':"a Portuguese",
	   'follow':562},

	  {'name':"Dhanush",
	   'job':"Film Actor",
	   'from':"an India",
	   'follow':5.5}
	]

#Program Starts Here

#Function for information extraction
def infoAndFollow():
	for i in range(0,total_score):
		info.append(DATA[i]['name']+' '+DATA[i]['from']+' '+DATA[i]['job'])
		folo.append(DATA[i]['follow'])

#Function for option list and Answer Generation
def optionListGenerator():
	option_a = [info[0]]
	option_b = [info[1]]
	Ans = []
	current_higher_folo = folo[0]
	current_higher_info = info[0]
	for i in range(0,total_score-2):
		if current_higher_folo>folo[i+1]:
			option_a.append(current_higher_info)
			option_b.append(info[i+2])
			Ans.append('A')
		elif current_higher_folo<folo[i+1]:
			current_higher_folo = folo[i+1]
			current_higher_info = info[i+1]
			option_a.append(current_higher_info)
			option_b.append(info[i+2])
			Ans.append('B')
	if current_higher_folo > folo[-1]:Ans.append('A')
	else: Ans.append('B')
	opt_1.extend(option_a)
	opt_2.extend(option_b)
	Answer.extend(Ans)
	
#Empty Initializations
info = []
folo = []
opt_1 = []
opt_2 = []
Answer = []
score = 0
total_score = len(DATA)

#Function Calls
infoAndFollow()
optionListGenerator()

#Output Presentation
print("WELCOME TO HIGHER OR LOWER\nChoose the one with most instagram followers.")
for i in range(0,total_score-1):
	user_input = input(f" A:{opt_1[i]} Vs B:{opt_2[i]} :")
	if user_input == Answer[i]:
		score+=1
		print(f"Your score is {score}")
	else:
		print(f"You Lose :( Your final score is {score}")
		break
else:
	print("You win")
		

	
































