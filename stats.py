def word_count(words: str) -> int:
#   with open(bookpath) as f: -- this is also fine --
    return len(words.split())

def char_counter(words: str) -> int:
#   
    char_count = {}
    for char in words:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count