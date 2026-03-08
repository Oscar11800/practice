from collections import Counter
from typing import Counter as CounterType

# takes two strings and returns a Counter object that counts the occurences of each character in the two strings combined.
def count_chars(s1: str, s2: str) -> CounterType:
    counter = Counter(s1)
    counter.update(s2)
    return counter
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
