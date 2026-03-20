from typing import List
from test_runner import assert_equal, run_tests

'''
271. Encode and Decode Strings

Design an algorithm to encode a list of strings into a single string and decode it back.

Implement:
- encode(strs: List[str]) -> str
- decode(s: str) -> List[str]

The decoded list must exactly match the original list.

Example 1:
  Input: ["Hello","World"]
  Output after decode: ["Hello","World"]

Example 2:
  Input: [""]
  Output after decode: [""]

Constraints:
  0 <= len(strs) < 100
  0 <= len(strs[i]) < 200
  Strings may contain any of 256 ASCII characters.
'''


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encode list of strings into one string.

        :param strs: List of strings.
        :return: Encoded string.
        """
        encoded = ""
        for s in strs:
            encoded += "[" + str(len(s)) + "]" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decode encoded string back into list of strings.

        :param s: Encoded string.
        :return: Original list of strings.
        """
        rtn = []
        i = 0
        n = len(s)
        while i < n:
            j = i + 1
            while j < n and s[j] != "]":
                j += 1
            length = int(s[i+1:j])
            start = j + 1
            end = start + length
            rtn.append(s[start:end])
            i = end
        return rtn


# ========== TESTS ==========

def test_example1():
    """Roundtrip with normal words."""
    codec = Solution()
    inp = ["",""]
    encoded = codec.encode(inp)
    decoded = codec.decode(encoded)
    assert_equal(decoded, inp)


def test_example2():
    """Roundtrip with empty string element."""
    codec = Solution()
    inp = [""]
    encoded = codec.encode(inp)
    decoded = codec.decode(encoded)
    assert_equal(decoded, inp)


if __name__ == "__main__":
    run_tests()