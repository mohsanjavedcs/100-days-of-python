import pandas as pd

df = pd.read_csv("_nato_phonetic_alphabet.csv")

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

codes = {
    row.letter: row.code for (index, row) in df.iterrows()
}

name = input("Enter your name: ").upper()

name_code = [codes[letter] for letter in name]

print(name_code)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

