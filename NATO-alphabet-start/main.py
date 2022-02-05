import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
words_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input('Enter a word:').upper()
try:
    list_for_input = [words_dict[letter] for letter in word]
except KeyError:
    print('Please, enter only letters.')
else:
    print(list_for_input)


