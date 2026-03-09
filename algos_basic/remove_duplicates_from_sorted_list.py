from test_runner import run_tests
from test_runner import assert_equal

'''
You are given an integer array nums sorted in non-decreasing order. 
Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k,
such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.
'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for val in nums[1:]:
            if val != nums[write]:
                write += 1
                nums[write] = val
        return write + 1

sol = Solution()

def test1():
    nums = [1,1,2,3,4]
    output = [1,2,3,4]
    result = sol.removeDuplicates(nums)
    assert_equal(result, len(output))



def test2():
    nums = [2,10,10,30,30,30]
    output = [2,10,30]
    result = sol.removeDuplicates(nums)
    assert_equal(result, len(output))

if __name__ == "__main__":
    run_tests()