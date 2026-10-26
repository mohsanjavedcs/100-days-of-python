#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as p_names:
    for name in p_names.readlines():
        names.append(name.strip())

letter = ""
with open("./Input/Letters/starting_letter.txt") as letters:
    for line in letters.readlines():
        letter += line

for name in names:
    letters = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/LetterTo{name}", mode="w") as l:
        l.write(letters)

print(letters)