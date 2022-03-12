# PIC 16A Final Project
# Group Members: Angela Xu, Angus Wu
# Player.py
# Player, HumanPlayer, ComputerPlayer Class

import random

class Player:
    '''
    Player class that checks whether the player's moves are valid or not.
    '''
    def __init__(self, name):
        '''
        When initialized, will save the name as self.name.
        '''
        self.name = name

    def validMove(self, moveX, moveY, grid):
        '''
        Checks the validity of the player's moves by scanning whether it is within
        the dimensions of the grid and if a player has not already moved at the
        specified location.
        Args:
            moveX: the X coordinate of the move
            moveY: the Y coordinate of the move
            grid: the game board
        Returns:
            True if the move position is empty
            False if the move position is occupied OR if the position is out of bounds
        '''
        if (moveX > len(grid) or moveY > len(grid[0])):
            #If the position is out of bounds
            return False
        elif (moveX < 0 or moveY < 0):
            #If the position is out of bounds
            return False
        elif (grid[moveX][moveY] == " X " or grid[moveX][moveY] == " O "):
            #If the position already is occupied
            return False
        elif (grid[moveX][moveY] == " . "):
            #If the move position is empty
            return True

        
class HumanPlayer(Player):
    '''
    Class that represents human players, and defines functions
    that allow the human player to make their moves.
    '''
    
    def makeMove(self, logo, grid):
        '''
        Prompts the user for X and Y coordinates of the position they want to
        move to and checks the validity of that move.
        Args:
            logo: the player's symbol
            grid: the game board
        Returns:
            a tuple representing the position of the player's move
        '''
        while True:
            try:
                #Prompts the player for the row move
                print(self.name + ", please enter the row you wish to play at (Starts at 0): ")
                rowChoice = input()
                rowChoice = int(rowChoice)
                
                #Prompts the player for the column move
                print(self.name + ", please enter the column you wish to play at (Starts at 0): ")
                columnChoice = input()
                columnChoice = int(columnChoice)
            
                #Checks if the user move is a valid move
                if (self.validMove(rowChoice, columnChoice, grid)):
                    #If a valid move, make the move on the grid
                    grid[rowChoice][columnChoice] = logo
                    return (rowChoice, columnChoice)
                else:
                    #If not a valid move, prompts user again for an appropriate move
                    print("User input is invalid. Please check that the move is not out of bounds, or already occupied")
            except ValueError:
                print("This function only supports integer inputs. Please try again.")
                

class ComputerPlayer(Player):
    '''
    A class that represents the computer player, which is created when
    there is only one player.
    '''
    
    def __init__(self):
        '''
        When initialized, this class will create the instance variable of
        the name as "Computer".
        Args:
            None
        Returns:
            None
        '''
        #By default, set the name of the computer player to be "Computer"
        self.name = "Computer"
    
    def makeMove(self, logo, grid):
        '''
        Randomly generates a valid move for the computer to make 
        after the player's turn.
        Args:
            logo: the computer player's symbol
            grid: the game board
        Returns:
            move: the computer's move
        '''
        #Find all possible moves and save into a list
        possibleMoves = self.findMoves(grid)
        
        #Pick a random move from the list
        move = random.choice(possibleMoves)
        
        #Make the move on the grid
        grid[move[0]][move[1]] = logo
        
        #Display the message where the computer moved
        print("The computer moved at row " + str(move[0]) + " and column " + str(move[1]))

        #Return move so that the Board class can evaluate if the computer won
        return move

    def findMoves(self, grid):
        '''
        Function that will find the empty spots in the game Board where the
        computer can place a valid move.
        Args:
            grid: the game board
        Returns:
            possibleMoves: a list of tuples that has all possible valid moves
        '''
        
        #Initialize an empty list
        possibleMoves = []
        
        #Iterating through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #If the grid is empty at this position
                if grid[i][j] == " . ":
                    #Store position into a list
                    possibleMoves.append((i, j))
                    
        return possibleMoves