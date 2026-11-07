from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    number_of_appearances = 0
    for list_item in nums:
        if list_item == x:
            number_of_appearances += 1
    return number_of_appearances



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
