import pandas

data = pandas.read_csv(
    "Day 30/273 NATO-Phonetic-Alphabet-for-the-Code-Exercise/nato_phonetic_alphabet.csv"
)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please input only letters.")
    else:
        print(output_list)
        break
