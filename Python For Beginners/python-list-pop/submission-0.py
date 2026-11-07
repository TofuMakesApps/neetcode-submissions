from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    # It should remove the element at the given index from my_list and return the modified list.
    my_list.pop(index)
    return my_list



def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    #It should pop the last n elements from my_list and return the modified list.
    i = 0
    while i < n:
        length = len(my_list)
        my_list.pop(length - 1)
        i += 1
    return my_list


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
