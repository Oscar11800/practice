from typing import List

# takes an integer and returns the integer if it is greater than or equal to 0. Otherwise, it should return 0.
def disallow_negatives(num: int) -> int:
    pass

# takes a list of integers and returns the maximum difference 
# between any two adjacent elements in the list, by subtracting the element on the right from the element on the left.
# In other words, it should return the maximum value of nums[i] - nums[i - 1] for all valid indices i.
def max_difference(nums: List[int]) -> int:
    pass 



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
