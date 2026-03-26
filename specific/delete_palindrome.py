
# Given a string s, return true if the s can be a palindrome after deleting at most one character from it.

def canBePalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    skipped = False
    while left < right:
        if s[left ] != s[right]:
            if skipped:
                return False
            elif s[left + 1] == s[right]:
                skipped = True
                left += 1
            elif s[right - 1] == s[left]:
                skipped = True
                right -= 1
            else:
                return False
        else:
            left += 1
            right -= 1
    return True


# Ex: [racedcar]
print(f"{canBePalindrome("racedcar")}") # true
print(f"{canBePalindrome("abba")}") # true
print(f"{canBePalindrome("")}")    # true
print(f"{canBePalindrome("cseattac")}") # false

# Strat:
# So brute force solution is to first just check if it can be a palindrome
# and then if it's not a palindrome, we can go and for loop over each character
# and delete one and check if it's a palindrome and if both cases are false then
# this is not a palindrome. This is On for the first palindrome check 
# And then On^2 for the second for looped palindrome check.
#
# Strat 2:
# So let's use 2 pointers like the optimal solution for regular palindrome problems. This time
# what we can do is have two pointers, left = 0 , right = len(s) - 1 and then we check that they 
# equal each other, and if at any point they do not equal each other, I will attempt to "skip"
# either the right or the left pointer (first I can check if the right decremented would equal the left,
# then I would check if the left incremented would equal the right) if either of those are true, I would do 
# that action and then continue checkign until left >= right. I will also need a flag to tell me when this
# has alread happened once. If it has alr happened and we need it to happen again, then we rtn False.
# Otherwise we return True
