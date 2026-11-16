import pandas as pd

df = pd.read_csv("_nato_phonetic_alphabet.csv")

codes = {
    row.letter: row.code for (index, row) in df.iterrows()
}

def generate():
    name = input("Enter your name: ").upper()
    try:
        name_code = [codes[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(name_code)

generate()