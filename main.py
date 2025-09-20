def get_book_text(bookpath):
    with open(bookpath, encoding='utf-8') as f:
        return f.read()

def main():
    bookpath = "books/frankenstein.txt"

    booktext = get_book_text(bookpath)

    num_words = len(booktext.split())

    print(f"{num_words} words found in the document")

main()