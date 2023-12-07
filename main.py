def main():
    path = "books/frankenstein.txt"
    text = open_book(path)
    words = get_num_words(text)
    chars = get_char_count_dict(text)
    print_report(path, words, chars)

def get_num_words(text):
    return len(text.split())

def get_char_count_dict(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def open_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    chars_list = list(chars.items())
    chars_list.sort(key = lambda x: x[1], reverse = True)
    for char in chars_list:
        if char[0].isalpha():
            print(f"the {char[0]} was found {char[1]} times")

main()