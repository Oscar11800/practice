'''
Please see the starter code of the Pet class and complete the following in the feed method:

Decrease the pet's hunger by 1
Print the string 'Fluffy has been fed.'.
Print the current hunger level of my_pet, in this format: 'Fluffy's hunger level: X'
And then call the feed method three times on my_pet.


'''
class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
