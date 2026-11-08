from typing import List

def read_integers() -> List[int]:
    user_input = input().split(",")
    return_list = []
    for i in user_input:
        return_list.append(int(i))

    # the_list = user_input.split(",")

    return return_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
