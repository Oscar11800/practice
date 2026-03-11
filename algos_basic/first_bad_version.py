from test_runner import assert_equal, run_tests

'''
278. First Bad Version

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of
calls to the API.

Example 1:
  Input: n = 5, bad = 4
  Output: 4
  Explanation: isBadVersion(3)->false, isBadVersion(5)->true, isBadVersion(4)->true

Example 2:
  Input: n = 1, bad = 1
  Output: 1

Constraints:
  1 <= bad <= n <= 2^31 - 1
'''

# For testing: set _bad before each test; isBadVersion() uses it
_bad = 0


def isBadVersion(version: int) -> bool:
    """Pre-defined API. Returns True if version >= _bad."""
    return version >= _bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Find the first bad version in [1, n] using the isBadVersion() API.

        :param n: Total number of versions.
        :return: The first bad version number.
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            is_bad = isBadVersion(mid)
            if is_bad and mid == 1:
                return 1
            elif is_bad and not isBadVersion(mid-1):
                return mid
            elif is_bad:
                right = mid - 1
            else:
                left = mid + 1

        return 1


# ========== TESTS ==========

def test_example1():
    """Example 1: n=5, bad=4."""
    global _bad
    _bad = 4
    sol = Solution()
    assert_equal(sol.firstBadVersion(5), 4)


def test_example2():
    """Example 2: n=1, bad=1."""
    global _bad
    _bad = 1
    sol = Solution()
    assert_equal(sol.firstBadVersion(1), 1)


if __name__ == "__main__":
    run_tests()
