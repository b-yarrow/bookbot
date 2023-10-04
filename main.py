def get_text(filepath):
    with open("books/frankenstein.txt") as f:
        return f.read()

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
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_text(book_path)

    word_count = count_words(text)

    print(f"{word_count} words found in the document ---")
    print("")

    letter_counts = count_letters(text.lower())

    letter_counts_list = []

    for letter in letter_counts:
        letter_counts_list.append((letter_counts[letter], letter))
        
    letter_counts_list.sort(reverse=True)

    for i in range(0, len(letter_counts_list)):
        print(f"The '{letter_counts_list[i][1]}' character was found {letter_counts_list[i][0]} times")

    print(f"--- End report ---")

main()