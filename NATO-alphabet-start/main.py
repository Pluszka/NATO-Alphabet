import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
words_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input('Enter word:').upper()

list_for_input = [words_dict[letter] for letter in word]

print(list_for_input)


