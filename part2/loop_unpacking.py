from typing import List, Tuple

# takes a list of tuples. Each tuple represents the (name, score) of a student. Find the student with the highest score and return their name.
def best_student(scores: List[Tuple[str, int]]) -> str:
    high_student = ""
    high_score = 0
    for student, score in scores:
        if (score > high_score):
            high_score = score
            high_student = student
    return high_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
