from typing import List

#  takes an integer n and returns a list of all odd numbers from 1 to n (inclusive).
def create_list_of_odds(n: int) -> List[int]:
    return [i for i in range(1,n+1) if i % 2 != 0]


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
