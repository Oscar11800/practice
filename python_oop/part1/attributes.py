'''
You are given a Pet class and an object from that class whiskers.

Print the attributes of whiskers with the formatting below.
Decrease the hunger attribute by 3, and increase the energy attribute by 2.
Print the attributes of whiskers again with the formatting below.
'''
class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes
