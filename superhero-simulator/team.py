import random
from hero import *

class Team:

    def __init__(self, name="Hero Team"):
        self.name = name
        self.members = []
        self.living_members = []
        self.team_deaths = 0
        self.team_kills = 0

    def __repr__(self):
        return f"Team({self.name}, {self.members})"

    def add_death(self):
        ''' update team statistics when a member dies in battle
        '''
        self.team_deaths += 1
        message = f'A member of {self.name} has died!'

        print(message)
        return message

    def add_kill(self):
        ''' update team statistics when a member is victorious in battle
        '''
        self.team_kills += 1
        message = f'A member of {self.name} has defeated an opponent!'

        print(message)
        return message


    def add_hero(self, *args):
        ''' Use to add hero object(s) to team's members attribute
        '''

        new_heroes = 0

        for hero in args:

            if hero not in self.members:
                new_heroes += 1
                self.members.append(hero)
                self.living_members.append(hero)

        if new_heroes == 1:
            message = f'{self.name} has added one new team member!'

        else:
            message = f'{self.name} has added {new_heroes} new team members'
        print(message)
        return message

    def remove_hero(self, *args):
        ''' Use to remove hero object(s) from team's members attribute
        '''

        old_heroes = 0

        for hero in args:

            if hero in self.members:
                old_heroes += 1
                self.members.remove(hero)
                self.living_members.remove(hero)

        if old_heroes == 1:
            message = f'{self.name} has lost one team member!'

        else:
            message = f'{self.name} has lost {old_heroes} team members!'

        print(message)
        return message

    def revive_team(self):
        ''' will allow the entire team to be revived and have their current health reset
        '''

        for hero in self.members:
            hero.current_health = hero.starting_health

            if hero not in self.living_members:
                self.living_members.append(hero)

        message = f"\n All of {self.name}'s members have been revived!"

        print(message)
        return message


    def view_all_heroes(self):
        ''' Use to view all hero object(s) in team's members attribute
        '''

        if not self.members:
            message = "There are no members on this team."

            print(message)
            return message
        
        else:

            for hero in self.members:
                message = f'{hero.name} is on team {self.name}'
                print(message)

            return self.members

    def attack(self, team):
        ''' take in another team object as a parameter. It will need to list each hero on both teams and randomly select a living hero from each team to fight. Update the list of living_heroes and living_opponents to reflect the result of the fight
        '''

        battling = True

        while battling:

            if not self.living_members or not team.living_members:
                message = "One or more teams do not have any members."
                
                print(message)
                battling = False

            team_member = random.choice(self.living_members)
            opponent = random.choice(team.living_members)

            print(f"\n\n\n{self.name}'s {team_member.name} will now battle {team.name}'s {opponent.name}!\n\n\n")

            winner = team_member.battle(opponent)

            if winner == team_member:
                self.add_kill()
                team.add_death()
                team.living_members.remove(opponent)

            elif winner == opponent:
                self.add_death()
                self.living_members.remove(team_member)
                team.add_kill()

            if self.living_members and not team.living_members:
                message = f'{self.name} has defeated {team.name}!'

                print(message)
                battling = False

            elif not self.living_members and team.living_members:
                message = f'{team.name} has defeated {self.name}!'

                print(message)
                battling = False

# Calls and variables used for Testing Below

# team = Team("Team 1")
# team2 = Team("Team 2")

# team.add_hero(hero, hero2)
# team2.add_hero(hero3, hero4)
# team.attack(team2)
# team.revive_team()
# team2.revive_team()
# team2.attack(team)
        
