def add_two_numbers() -> int:
    user_in = input().split(",")
    int_list = []

    for i in user_in:
        int_list.append(int(i))

    return sum(int_list)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
