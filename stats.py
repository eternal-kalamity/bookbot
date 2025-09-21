# sub file for bookbot

def sort_on(items):
    return items[1]

def word_count(words: str) -> int:
#   with open(bookpath) as f: -- this is also fine --
    return len(words.split())

def char_counter(words: str) -> list[tuple[str, int]]:
#   makes empty list
    char_count = {}
#   for loop for every character in word
    for char in words:
        if char.isalpha():
#           converts all characters to lower case
            lower_char = char.lower()
#           gets characters from list if their and addeds 1 to each count
#           if not their adds character to the list 
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
#   covert the previous dictionary into a list    
    char_items = list(char_count.items())

    return char_items