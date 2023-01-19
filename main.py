import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def create_phonetic_words():
    try:
        word = input("Choose a word: ").upper()
        words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Use a real word")
        return create_phonetic_words()
    else:
        return words
print(create_phonetic_words())