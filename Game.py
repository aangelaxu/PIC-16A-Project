# PIC 16A Final Project
# Group Members: Angela Xu, Angus Wu
# Game.py
# Game Class


from Board import Board
from Player import Player, HumanPlayer, ComputerPlayer

class Game:
    '''
    A class representing the game itself. Allows players to create the game.
    '''
    def __init__(self):
        '''
        Creates the Game object but does not initialize any class variables.
        '''
        pass
    
    def CreateGame(self):
        '''
        Creates Game by prompting user to specify Game conditions 
        including grid size, win conditions, and number of players.
        '''
        
        print("Welcome to Variable Tic Tac Toe.")
        
        #Prompts the user for an input for grid size
        while True:
            try:
                print("What size n * n you like the grid to be? (Must be between 3 and 20)")
                gridSize = input()
                gridSize = int(gridSize)
            
                if gridSize > 20 or gridSize < 3:
                    print("Invalid grid, please try again.")
                else:
                    break
            except ValueError:
                print("This function only takes integer inputs. Please restart the game.")
        
        #Prompts the user for an input for winning length/condition
        while True:
            try:
                print("How many to connect in order to win? (Must be at least 3, and less than or equal to the grid size)")
                winLen = input()
                winLen = int(winLen)
            
                if winLen > gridSize or winLen < 3:
                    print("Invalid win condition. Please try again")
                else:
                    break
            except ValueError:
                print("This function only takes integer inputs. Please restart the game.")
        
        #Prompts the user for number of players
        while True:
            print("How many players will be playing?")
            numPlayers = input()
            
            if numPlayers == "2":
                print("Please enter the name of Player 1 (Player 1 will go first):")
                play1Name = input()
                print("Please enter the name of Player 2 (Player 2 will go second):")
                play2Name = input()
                
                #Initialize the board and players based on user inputs
                BoardGame = Board(gridSize, gridSize, winLen, HumanPlayer(play1Name), HumanPlayer(play2Name))
                
                break
             
            #If there is only one player (There will be a computer player)
            if numPlayers == "1":
                print("Please enter the your name:")
                play1Name = input()
                
                #Prompt the user whether or not to move first
                while True:
                    print("Would you like to move first? (Y or N)")
                    firstMove = input()
                    
                    if firstMove == "Y":
                        #Initialize the board and players based on user inputs
                        BoardGame = Board(gridSize, gridSize, winLen, HumanPlayer(play1Name), ComputerPlayer())
                        break
                    elif firstMove == "N":
                        #Initialize the board and players based on user inputs
                        BoardGame = Board(gridSize, gridSize, winLen, ComputerPlayer(), HumanPlayer(play1Name))
                        break
                    else:
                        print("Invalid input, please try again")
            
            
            else:
                print("This game only supports 1 or 2 players. Please try again.")
                
        #Start the game
        BoardGame.playGame()