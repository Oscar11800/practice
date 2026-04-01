import json
from collections import Counter
import heapq
# Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))

# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]

# create a function that finds the ten most spoken languages
# create a function that creates a list of the ten most populated countries

file_path = 'data/countries_data.json'
def find_most_spoken():
    with open(file_path, 'r') as file:
        counter = Counter()
        all = json.load(file)
        for dict in all:
            counter.update(dict['languages'])
        print(type(dict))
        print(counter)
        return [(count, item) for item, count in counter.most_common(10)]
        # breakpoint()

def get_most_populated():
    populations = []
    rtn = []
    with open(file_path, 'r') as file:
        all = json.load(file)
    print(type(all))
    for country in all:
        heapq.heappush(populations, (-country['population'], country['name']))
    for i in range(10):
        rtn.append((-heapq.heappop(populations)[0], ))
    return rtn
        

print(find_most_spoken())
print(get_most_populated())