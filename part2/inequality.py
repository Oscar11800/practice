from typing import List

# return True if the length of the names list is greater than 0 and less than or equal to the parameter max_length. Otherwise it should return False.
def is_arr_valid(names: List[str], max_length: int) -> bool:
    pass



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
