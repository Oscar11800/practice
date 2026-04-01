# read obama count number of lines and words

file_path = 'data/obama.txt'

def count_words():
    with open(file_path, 'r') as file:
        words = len(file.read())
        return words
def count_lines():
    with open(file_path, 'r') as file:
        lines = file.readlines()
        breakpoint()
        return len(lines)

print(count_lines())
print(count_words())