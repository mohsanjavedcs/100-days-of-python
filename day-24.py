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