from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    list_length = len(words)
    set_length = len(my_set)
    if list_length > set_length:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
