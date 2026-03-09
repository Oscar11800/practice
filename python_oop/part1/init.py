'''
We have a Pet class, but its __init__ method is missing. 
Currently, the code will produce the following error when you try to run it.

TypeError: Pet() takes no arguments
Your task is add the __init__ method to the Pet class to initialize the name,
species, and age attributes when a new pet is created.


'''

class Pet:
    # TODO: Implement the __init__ method here
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age


# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")
