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
        if len(strs) == 0:
            return encoded
        for s in strs:
            s_str = "[" + str(len(s)) + "]" + s
            encoded += s_str
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decode encoded string back into list of strings.

        :param s: Encoded string.
        :return: Original list of strings.
        """
        rtn = []
        i = 1
        while i < len(s):
            s_len = ""
            while s[i] != ']':
                s_len += s[i]
                i += 1
            s_len = int(s_len)
            i+= 1
            new_s = ""
            for i in range(i, i + s_len):
                new_s += s[i]
            rtn.append(new_s)
            if s_len > 0:
                i+= 2
            else:
                i += 1
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