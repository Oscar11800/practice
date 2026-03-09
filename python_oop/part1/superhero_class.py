'''
In this challenge, you'll complete the implementation of a SuperHero class and create superhero instances. 
Your tasks are as follows:

1. Complete the SuperHero class:

Add attributes name, power, and health to the __init__ method.
2. Create superhero instances:

Instantiate a superhero with the name "Batman", power "Intelligence", and health 100.
Instantiate a superhero with the name "Superman", power "Strength", and health 150.
3. Display superhero information:

Print out each superhero's name, power, and health on a separate line.
Note: You can remove the pass in the __init__ method after adding your code.
'''
class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health
    
    def print_superhero(self):
        print(self.name)
        print(self.power)
        print(self.health)


# TODO: Create Superhero instances
batman = SuperHero("Batman", "Intelligence", 100)
superman = SuperHero("Superman", "Strength", 150)




# TODO: Print out the attributes of each superhero
batman.print_superhero()
superman.print_superhero()