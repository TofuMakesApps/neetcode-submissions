def remove_fourth_character(word: str) -> str:
    a = word[:3]
    b = word[4:]
    new_string = a + b
    return new_string

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
