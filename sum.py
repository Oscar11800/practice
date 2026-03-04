from typing import List

def add(arr: List[int], target: int) -> List[int]:
    arr.sort()
    l_ptr = 0
    r_ptr = len(arr) - 1
    while l_ptr < r_ptr:
        s = arr[l_ptr] + arr[r_ptr]
        if s == target:
            return [arr[l_ptr], arr[r_ptr]]
        elif s < target:
            l_ptr += 1
        else:
            r_ptr -= 1
    return None