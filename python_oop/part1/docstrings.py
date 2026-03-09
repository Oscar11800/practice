'''
When you run the code, you'll see None printed for each docstring because they don't exist yet.
sYour tasks are as follows:

Write a class docstring describing what the Pet class represents.
Add a brief docstring to the __init__ method.
Add a docstring to the make_sound method explaining what it does.

'''
class Pet:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type

    def make_sound(self) -> str:
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)
