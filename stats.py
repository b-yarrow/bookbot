def sort_on(items):
    return items["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict ={}
    for char in text:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1

    return char_dict

def sort_chars(char_counts):
    char_counts_list = []

    for char in char_counts:
        char_counts_list.append({"char": char, "num": char_counts[char]})
        
    char_counts_list.sort(reverse=True, key=sort_on)

    return char_counts_list