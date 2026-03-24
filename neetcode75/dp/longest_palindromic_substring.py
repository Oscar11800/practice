from neetcode75.test_runner import assert_equal, run_tests

"""
Longest Palindromic Substring
Medium

Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings with the same length, return
any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:
Input: s = "abbc"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s contains only digits and English letters.
"""


class Solution:
    def isPalindrome(self, s:str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rtn = ""
        for i in range(n):
            left = right = i
            righteven = i + 1
            while right <= n-1 and left >= 0 and s[right] == s[left]:
                if (right - left + 1) > len(rtn):
                    rtn = s[left:right+1]
                left -= 1
                right += 1
            left = i
            while righteven <= n-1 and left >= 0 and s[righteven] == s[left]:
                if (righteven - left + 1) > len(rtn):
                    rtn = s[left:righteven+1]
                left -= 1
                righteven += 1
        return rtn

def test_example1():
    sol = Solution()
    result = sol.longestPalindrome("ababd")
    assert_equal(result in ["aba", "bab"], True)


def test_example2():
    sol = Solution()
    assert_equal(sol.longestPalindrome("abbc"), "bb")


# Run: python3 -m neetcode75.dp.longest_palindromic_substring
if __name__ == "__main__":
    run_tests()
