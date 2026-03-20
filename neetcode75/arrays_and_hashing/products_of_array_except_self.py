from typing import List
from test_runner import assert_equal, run_tests

'''
Products of Array Except Self

Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Thoughts: thinkin about the sol to this, I think I can solve this without divisioin operator by doing a sort of memoization
Let's look at the base case where there are only 2 elements. The first element would be just the second element and the
2nd element would be just the first element. For 3 elements, the first element of the rtn would be the 2nd x 3rd, and the
2nd would be 1st x 3rd and 3rd would be 1st x 2nd. 

the easiest solution would be to first loop through and ge the full product and then loop through again and get fp/[i] 
to get the value of the rtn at that index this would be a On solution but would use division.

The only way to achieve an On solution is to do single or multiple passthroughs (of a constant repetition) and without sort
if we have [0] = the full product, then have [1] = [0] 

The solution without using the division would be prefix and suffix which would take 2 pass throughs, one from l->r and
another from r->l. The l-> will have an array of size len nums and for each index we will store a moving product where
prefix[0] = nums[0] and [1] = nums[0]*nums[1] and so on so forth such that the final nums[len(nums)-1] would be
the full product. Then we similarly create another array with the suffix which will go in reverse order so that
suffix[0] = nums[-1] and suffix[len(nums) - 1] = full product. Finally with both of these arrays, we can work on our rtn array 
which we get by multiplying prefix and suffix at that i. So rtn[0] = prefix[0] * suffix[0] which is essentially 1 * 
full product without nums[0]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        """
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        rtn = [p * s for p, s in zip(prefix, suffix)]
        return rtn



# ========== TESTS ==========

def test_example1():
    sol = Solution()
    input = [1,2,4,6]
    output = sol.productExceptSelf(input)
    expected = [48,24,12,8]
    assert_equal(output, expected)


def test_example2():
    sol = Solution()
    input = [-1,0,1,2,3]
    output = sol.productExceptSelf(input)
    expected = [0,-6,0,0,0]
    assert_equal(output, expected)


if __name__ == "__main__":
    run_tests()