import random
from ability import *

class Weapon(Ability):

    def __repr__(self):
        return f"Weapon({self.name}, {self.max_damage})"

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """

        half_damage = self.max_damage / 2
        attack_value = random.randrange(half_damage, self.max_damage)
        message = f'{self.name}: weapon attack is {attack_value}'

        print(message)
        return attack_value