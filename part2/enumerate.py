from typing import List

# returns the index of the first occurrence of the number 7 in the list nums, or -1 if 7 is not found.
def get_index_of_seven(nums: List[int]) -> int:
    index = -1
    for i, num in enumerate(nums):
        if num == 7:
            return i
    return index

# returns the distance between the first and second occurrence of the number 7 in the list nums.
def get_dist_between_sevens(nums: List[int]) -> int:
    index1 = -1
    index2 = -1
    for i, num in enumerate(nums):
        if num == 7:
            if index1 == -1:
                index1 = i
            elif index2 == -1:
                index2 = i
    return index2 - index1


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
