#import os
from stats import word_count, char_counter, sort_on

def get_book_text(bookpath):
    with open(bookpath, encoding='utf-8') as f:
        return f.read()

def main():
    bookpath = "books/frankenstein.txt"

    booktext = get_book_text(bookpath)

    num_words = word_count(booktext)

    char_counts = char_counter(booktext)

#   sort the new list
    sorted_char_count = sorted(char_counts, key=sort_on, reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
#    for char in char_count:
    for char, count in sorted_char_count:
        print(f"{char}: {count}")

    print("============= END ===============")
main()