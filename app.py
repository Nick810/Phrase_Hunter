# Import your Game class
from phrasehunterNICK.game import PHRASES_LIST
from phrasehunterNICK.game import Game
# Create your Dunder Main statement.

if __name__ == '__main__':
    run = Game(PHRASES_LIST)
    run.welcome()
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
