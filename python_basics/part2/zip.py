from typing import List, Dict


# that takes two lists, names and scores, and returns a dictionary where the key is names[i] and it maps to scores[i] as the value.
def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    rtn = {}
    for name, score in zip(names, scores):
        rtn[name] = score
    return rtn


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))

# zip creation and space is O(1), set at the beginning of the input lists