import random

class Ability:

    def __init__(self, name='Ability/Weapon' , max_damage=100):
        self.name = name
        self.max_damage = max_damage

    def __repr__(self):
        return f"Ability({self.name}, {self.max_damage})"

    def attack(self):
        ''' We don't want our Hero to have the same attack value every time. We want to have some range of values that are possible when our Hero attacks. return a random value between 0 and the strongest attack an ability can produce, max_damage
        '''
        attack_value = random.randrange(0, self.max_damage)
        message = f'{self.name}: attack is {attack_value}'

        print(message)
        return attack_value




