from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output
and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Current solution loops through nested to get the sum between every element to generate negative targets
        we store the indices of the nums that created these targets. Then we loop through the nums again to
        check if they are a target that are not from the original nums, and if they are, they we append all 3 nums.
        Finally we sort the values of each of these in the list of lists and convert them to tuple so we can
        convert it to set to remove dupes, finally return the list version
        '''
        rtn = []
        targetmap = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                target = -(nums[i] + nums[j])
                targetmap.setdefault(target, []).append((i, j))
        for idx, num in enumerate(nums):
            if num not in targetmap:
                continue
            for (i, j) in targetmap[num]:
                if idx != i and idx != j:
                    rtn.append([nums[i], nums[j], nums[idx]])
        return [list(t) for t in {tuple(sorted(x)) for x in rtn}]
        


def normalize_triplets(triplets: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(t) for t in triplets])


def test_example1():
    sol = Solution()
    actual = sol.threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert_equal(normalize_triplets(actual), normalize_triplets(expected))


def test_example2():
    sol = Solution()
    assert_equal(sol.threeSum([0, 1, 1]), [])


def test_example3():
    sol = Solution()
    assert_equal(sol.threeSum([0, 0, 0]), [[0, 0, 0]])


if __name__ == "__main__":
    run_tests()
