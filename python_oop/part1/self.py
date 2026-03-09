'''
You are given a Superhero class with a power_boost method that is not working correctly. 
When you run this code, you'll encounter the following error:

TypeError: power_boost() takes 1 positional argument but 2 were given
Your task is to identify the issue and fix it and get the expected output.


'''
class SuperHero:
    def __init__(self, name: str, power: str, strength: int):
        self.name = name
        self.power = power
        self.strength = strength
    
    def power_boost(self) -> None:
        self.strength += strength_increase
        print(f"{self.name}'s strength increased to {self.strength}!")



# Don't modify the following code
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

ironman.power_boost(15)
