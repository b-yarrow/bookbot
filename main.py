def get_text(filepath):
    with open("books/frankenstein.txt") as f:
        return f.read()
        
        #print(len(words))
        return len(words)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict ={}
    for letter in alphabet:
        letter_dict[letter] = text.count(letter)
    return letter_dict

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]


def main():
    text = get_text("books/frankenstein.txt")
    
    letter_counts = count_letters(text.lower())

    for letter in letter_counts:
        count = letter_counts[letter]
        print(f"{letter} appears {count} times.")


main()