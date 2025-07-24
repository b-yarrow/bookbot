def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict ={}
    for letter in alphabet:
        letter_dict[letter] = text.count(letter)
    return letter_dict