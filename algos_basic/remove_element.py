from test_runner import assert_equal, run_tests

'''
You are given an integer array nums and an integer val.
Your task is to remove all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements,
say k, such that the first k elements of nums do not contain val.

Note:

The order of the elements which are not equal to val does not matter.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain only elements not equal to val.
Return k as the final result.
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while(val in nums):
            nums.remove(val)
        return len(nums)
        

# ========== TESTS ==========
sol = Solution()

def test1():
    nums1 = [1,1,2,3,4]
    val1 = 1
    result = sol.removeElement(nums1, val1)
    assert_equal(result, 3)



def test2():
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    result = sol.removeElement(nums2, val2)
    assert_equal(result, 5)

if __name__ == "__main__":
    run_tests()