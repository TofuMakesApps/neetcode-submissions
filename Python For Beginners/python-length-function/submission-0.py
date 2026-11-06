def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2):
        return word1
    else:
        return word2    
# It takes two words (strings) as parameters, and returns the longer word. If the words are the same length, return the first word.

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
