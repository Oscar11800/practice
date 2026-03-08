from typing import List


def get_word_length(word: str) -> int:
    return len(word)

# This function accepts a list of words and returns a new list of words sorted based on their length, in descending order.
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word:len(word), reverse=True)
    return words

# This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value, in ascending order. Hint: You may use the abs() function to get the absolute value of a number.
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=abs)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
