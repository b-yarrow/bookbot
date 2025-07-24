import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    #book_path = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}... ")
    text = get_text(book_path)

    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = count_chars(text)

    sorted_chars = sort_chars(char_counts)

    for i in range(0, len(sorted_chars)):
        if sorted_chars[i]["char"].isalpha():
            print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["num"]}")

    print("============= END ===============")

main()