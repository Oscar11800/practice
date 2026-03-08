from typing import List

# takes three integers rows, cols, and value.
# It returns a 2-D list of size rows x cols where each element is equal to value.
def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    return [[value]*cols for _ in range(rows)]


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
