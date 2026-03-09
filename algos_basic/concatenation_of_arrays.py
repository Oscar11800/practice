from test_runner import assert_equal, run_tests

'''
You are given an integer array nums of length n.
Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
'''
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * 2 * n

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num
        return ans
        
sol = Solution()

def test1():
    nums = [1,4,1,2]
    output = [1,4,1,2,1,4,1,2]
    result = sol.getConcatenation(nums)
    assert_equal(result, output)



def test2():
    nums = [22,21,20,1]
    output = [22,21,20,1,22,21,20,1]
    result = sol.getConcatenation(nums)
    assert_equal(result, output)

if __name__ == "__main__":
    run_tests()