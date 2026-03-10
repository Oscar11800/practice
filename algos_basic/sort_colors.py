from test_runner import assert_equal, run_tests

'''
75. Sort Colors (Dutch National Flag)

You are given an array nums consisting of n elements where each element is an integer
representing a color:

  0 = red
  1 = white
  2 = blue

Your task is to sort the array in-place such that elements of the same color are grouped
together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:
  Input: nums = [1,0,1,2]
  Output: [0,1,1,2]

Example 2:
  Input: nums = [2,1,0]
  Output: [0,1,2]
'''


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Sort nums in-place: reds (0), whites (1), blues (2).
        Do not return anything; modify nums in-place.
        """
        buckets = [0]*3
        for num in nums:
            buckets[num] += 1
        
        idx = 0
        for i in range(3):
            for n in range(buckets[i]):
                nums[idx] = i
                idx += 1


# ========== TESTS ==========

def test_example1():
    """Example 1: [1,0,1,2] -> [0,1,1,2]."""
    sol = Solution()
    nums = [1, 0, 1, 2]
    sol.sortColors(nums)
    assert_equal(nums, [0, 1, 1, 2])


def test_example2():
    """Example 2: [2,1,0] -> [0,1,2]."""
    sol = Solution()
    nums = [2, 1, 0]
    sol.sortColors(nums)
    assert_equal(nums, [0, 1, 2])


if __name__ == "__main__":
    run_tests()