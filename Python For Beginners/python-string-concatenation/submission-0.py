def concatenate(s1: str, s2: str) -> str:
    # accepts two strings as parameters and returns a new string that is the concatenation of the two input strings. If the length of the string after concatenating them is greater than 10, return "Too long!".
    my_str = s1 + s2
    if len(my_str) > 10:
        return "Too long!"
    else:
        return my_str




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
