from typing import List

#  takes a 2D grid grid and two integers r and c, where r is the index of a row and c is the index of a column. 
# It should return True if the cell at row r and column c is within the bounds of the grid, and False otherwise.
def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    realr = len(grid)
    realc = len(grid[0])
    if (not (0 <= r <= realr)) or (not (0 <= c <= realc)):
        return False
    return True


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
