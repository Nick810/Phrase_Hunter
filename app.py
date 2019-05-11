# Import your Game class
from phrasehunter.game import Game

# Create your Dunder Main statement.
if __name__ == '__main__':
    ph = Game(PHRASES_LIST)
    ph.welcome()
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
