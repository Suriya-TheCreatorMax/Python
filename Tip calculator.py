print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
num = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total = bill + ((bill*tip)/100)
splitUp = total/num
print("Each person should pay: $",splitUp)
