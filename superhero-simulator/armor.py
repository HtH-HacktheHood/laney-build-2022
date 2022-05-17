import random

class Armor:

    def __init__(self, name='Armor', max_block=100):
        self.name = name
        self.max_block = max_block

    def __repr__(self):
        return f"Armor({self.name}, {self.max_block})"

    def block(self):
        ''' like the Ability class attack() method, returns a number between 0 and your max_block attribute. 
        '''
        defense_value = random.randrange(0, self.max_block)
        message = f'{self.name}: defense is {defense_value}'

        print(message)
        return defense_value