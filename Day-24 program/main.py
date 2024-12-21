#Author : Susindhar M
#Date   : 21/12/2024
#Practice for file handling

#Initialization
name_list = []

#Opening and reading the original letter and names
with open("./Input/Letters/starting_letter.txt") as original_letter:
    names = open("./Input/Names/invited_names.txt", mode = "r")
    name_list = names.read().splitlines()
    names.close()
    content = original_letter.read()

    #Creating files with modified content
    for names in name_list:
        new_content = content.replace('[name]', names)
        filepath = "./Output/ReadyToSend/" + names + ".txt"
        new_file = open(filepath, mode = "w")
        new_file.write(new_content)
        print(names)
        new_file.close()
