def get_book_text(bookpath):
    with open(bookpath, encoding='utf-8') as f:
        return f.read()

def main():
    bookpath = "books/frankenstein.txt"

    booktext = get_book_text(bookpath)

    print(booktext)

main()