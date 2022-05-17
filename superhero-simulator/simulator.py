from ability import *
from weapon import *
from arena import *
from armor import *
from hero import *
from team import *

game_is_running = True

# Instantiate Game Arena
arena = Arena()

# Welcome the user to the battle simulator
print("\nWelcome to the Superhero Battle Simulator! Here you can create and fully customize your own warriors with custom abilities, weapons, and armor! You can then put your heroes on teams and have them do battle against each other! Follow the prompts and have fun! May you be victorious!\n\n\n")

#Build Teams
arena.build_team_one()
arena.build_team_two()

# Start of Battle Simulator
while game_is_running:

    # heroes on respective teams do battle
    arena.team_battle()

    # stats from the hero battles are tracked and displayed
    arena.show_stats()

    # give user option to play again
    play_again = input("\nPlay Again? Y or N:  ")

    #Check for Player Input
    if play_again.lower() == "n":
        game_is_running = False

    else:
        #Revive heroes to play again
        arena.team_one.revive_team()
        arena.team_two.revive_team()