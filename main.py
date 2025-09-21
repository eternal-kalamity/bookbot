#import os
from stats import word_count, char_counter

def get_book_text(bookpath):
    with open(bookpath, encoding='utf-8') as f:
        return f.read()

def main():
    bookpath = "books/frankenstein.txt"

    booktext = get_book_text(bookpath)

    num_words = word_count(booktext)

    char_count = char_counter(booktext)

    print(f"{num_words} words found in the document")

#    for char in char_count:
    print(f"{char_count}")

main()