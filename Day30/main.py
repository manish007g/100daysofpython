# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
ans=1
while ans > 0:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter letters in alphabets only")
    else:
        print(output_list)
        ans=0
