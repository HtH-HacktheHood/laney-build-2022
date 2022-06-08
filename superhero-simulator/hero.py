import random

from pyparsing import empty
from ability import *
from armor import *
from weapon import *

# hero.py
class Hero:
    
    def __init__(self, name='Hero', starting_health=1000):
        
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []
        self.deaths = 0
        self.kills = 0

    def __repr__(self):
        return f"Hero({self.name})"

    def add_armors(self, *args):
        ''' to be able to append armors to the heros armor list
        '''
        
        new_armors = 0

        for armor in args:

            if armor not in self.armors:
                new_armors += 1
                self.armors.append(armor)

        if new_armors == 1:
            message = f'{self.name} equipped a new piece of armor!'

        else:
            message = f'{self.name} equipped {new_armors} new pieces of armor!'

        print(message)
        return message

    def add_abilities(self, *args):
        ''' to be able to append abilities to the heros ability list
        '''
        
        new_abilities = 0

        for ability in args:

            if ability not in self.abilities:
                new_abilities += 1
                self.abilities.append(ability)

        if new_abilities == 1:
            message = f'{self.name} learned 1 new ability!'

        else:
            message = f'{self.name} learned {new_abilities} new abilities!'

        print(message)
        return message

    def add_weapons(self, *args):
        ''' to be able to append weapons to the heros ability list
        '''
        
        new_weapons = 0

        for weapon in args:

            if weapon not in self.abilities:
                new_weapons += 1
                self.abilities.append(weapon)

        if new_weapons == 1:
            message = f'{self.name} can now use a new weapon!'

        else:
            message = f'{self.name} can now use {new_weapons} new weapons!'

        print(message)
        return message

    def add_death(self):
        ''' update hero statistics when they die in battle
        '''
        self.deaths += 1
        message = f'{self.name} has died!'

        print(message)
        return message

    def add_kill(self):
        ''' update hero statistics when they are victorious in battle
        '''
        self.kills += 1
        message = f'{self.name} has defeated an opponent!'

        print(message)
        return message

    def attack(self):
        ''' allows our hero to use the abilities that they have stored. This method should loop through your heros abilities and return a total damage count after adding the attack values of all the abilities
        '''

        total_attack = 0

        for ability in self.abilities:
            total_attack += ability.attack()

        message = f'{self.name}: total attack is {total_attack}'
        
        print(message)
        return total_attack

    def defend(self):
        ''' allows our hero to use armor that they have stored. This method should loop through their armors and return a total defense count
        '''

        total_defense = 0

        for armor in self.armors:
            total_defense += armor.block()

        message = f'{self.name}: total defense is {total_defense}'
        
        print(message)
        return total_defense

    def take_damage(self, incoming_damage):
        ''' change our hero's current_health based on the number and type of armor that they have against the attack of their opponent
        '''

        damage = incoming_damage - self.defend()

        if damage > 0:
            self.current_health -= damage

            if self.current_health > 0:
                message = f'{self.name} took {damage} points of damage! Their current health is {self.current_health}.'

            else:
                message = f'{self.name} took {damage} points of damage! Their current health is 0.'

        else:
            message = f'{self.name} took no damage! Their current health is {self.current_health}.'

        print(message)
        return message

    def battle(self, opponent):
        ''' First we need to check our heroes abilities. If no hero has abilities, print "Draw". Else, start the fighting loop until one contender loses all their health. The hero (self) and their opponent must attack each other and each must take damage from the other's attack. After each attack, check if either contender is alive
        '''

        if not self.abilities and not opponent.abilities:
            message = "No hero has any abilities. This fight is a draw!"

            print(message)
            return message

        battling = True
        turn = 0

        while battling:

            if turn % 2 == 0:
                print(f"\nTurn: {turn + 1}")
                opponent.take_damage(self.attack())

            if turn % 2 == 1:
                print(f"\nTurn: {turn + 1}")
                self.take_damage(opponent.attack())

            turn += 1

            if self.current_health <= 0:
                winner = opponent
                loser = self
                message = f'\n{winner.name} has defeated {loser.name} '

                self.add_death()
                opponent.add_kill()

                battling = False

                print(message)
                return winner

            if opponent.current_health <= 0:
                winner = self
                loser = opponent
                message = f'\n{winner.name} has defeated {loser.name} '

                self.add_kill()
                opponent.add_death()

                battling = False

                print(message)
                return winner