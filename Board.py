# PIC 16A Final Project
# Group Members: Angela Xu, Angus Wu
# Board.py
# Board class


from Player import Player, HumanPlayer, ComputerPlayer

class Board:
    '''
    A class that initializes the Tic Tac Toe Board for the Game,
    and runs the loop that the game is played through.
    '''
    def __init__(self, sizeX, sizeY, winLen, player1, player2):
        '''
        When initalized, this class will create all of the object variables, 
        initialize the empty grid, and tuples for the players' names and logos. 
        Args:
            sizeX: number of rows
            sizeY: number of columns
            winLen: win conditions
            player1: name of player 1
            player2: name of player 2
        Returns:
            None
        '''
        #Initializing all object variables
        self.x = sizeX
        self.y = sizeY
        self.winLen = winLen
        self.moveCounter = 0
        self.grid = []
        self.gridLines = (sizeX - 1) * "----" + "---"
        
        #Initialize the empty grid
        for i in range(sizeX):
            temp = []
            for j in range(sizeY):
                temp.append(" . ")
                
            self.grid.append(temp)

        #Creating player tuple and corresponding player logos        
        self.players = [player1, player2]
        self.logos = [" X ", " O "]
        
        
    def playGame(self):
        '''
        Runs the game and evaluates the moves until the game is over.
        Args:
            None
        Returns:
            None
        '''
        counter = 0
        self.displayBoard()
        
        #While True loop will keep running until the game is over
        while True:
            
            #Calls the appropriate player's makeMove() function with the appropriate player logo
            move = (self.players[counter % 2]).makeMove(self.logos[counter % 2], self.grid)
            
            #Displays the board after the move is made
            self.displayBoard()
            
            #Evaluates whether the game is over
            gameOver = self.gameOver(move[0], move[1], self.logos[counter % 2])
            
            #If the game is a tie (Board is full but no winners)
            if (gameOver == "tie"):
                print("The game has concluded with a tie")
                break
            #If the game is over
            elif (gameOver):
                #Print out congratulatory message and break out of the while loop
                print(self.players[counter % 2].name + " has won the game! Congratulations")
                break
            #If the game is not over
            elif not (gameOver):
                #Increment counter so that the next player moves
                counter += 1
                continue
 
            
    
    def displayBoard(self):
        '''
        Displays the board before and after each move is made.
        '''
        #Iterating through the board
        for i in range(self.x):
            for j in range(self.y):
                print(self.grid[i][j], end = "")
                #Print a divider in between columns
                if j != self.y - 1:
                    print("|", end = "")
            
            #Print a divider line in between rows
            if i != self.x - 1:
                print("\n" + self.gridLines)
                
        print("\n")
            
    
    def checkHorizontalWin(self, moveX, moveY, logo):
        '''
        Checks whether there has been a horizontal win after each
        move is made.
        Args:
            moveX: the X coordinate of the move
            moveY: the Y coordinate of the move
            logo: player symbol
        Returns:
            True if there is a horizontal win
            False if there is no horizontal win
        '''
        counter = 0
        
        #Scanning horizontally:
        for i in range(self.x):
            if self.grid[i][moveY] == logo:
                #If the logo matches the player that just moved, increment 1
                counter += 1
                #If the counter is equal to the winning condition
                if counter == self.winLen:
                    return True
            else:
                #If logo does not match the player that just moved, reset counter to 0
                counter = 0
                
        return False
    
    def checkVerticalWin(self, moveX, moveY, logo):
        '''
        Checks whether there has been a vertical win after each
        move is made.
        Args:
            moveX: the X coordinate of the move
            moveY: the Y coordinate of the move
            logo: player symbol
        Returns:
            True if there is a vertical win
            False if there is no vertical win
        '''
        counter = 0
        
        #Scanning vertically:
        for i in range(self.y):
            #If the logo matches the player that just moved, increment 1
            if self.grid[moveX][i] == logo:
                counter += 1
                #If the counter is equal to the winning condition
                if counter == self.winLen:
                    return True
            else:
                #If logo does not match the player that just moved, reset counter to 0
                counter = 0
                
        return False
    
    def checkDiagonalWin(self, moveX, moveY, logo):
        '''
        Checks whether there has been a diagonal win after each
        move is made by looking at both diagonal directions from the 
        move made using 2 different counters.
        Args:
            moveX: the X coordinate of the move
            moveY: the Y coordinate of the move
            logo: player symbol
        Returns:
            True if there is a diagonal win
            False if there is no diagonal win
        '''
        counterNW = 0
        counterNE = 0
        offset = 0
        
        #Scanning North-East Direction (INCLUSIVE OF THE MOVE THE PLAYER JUST MADE)
        #X decreases, Y increases
        for i in range(0, moveX + 1):
            #Checks that X and Y are not out of bounds
            if (moveX - i >= 0 and moveY + offset < self.y):
                if self.grid[moveX - i][moveY + offset] == logo:
                    counterNE += 1
                    offset += 1
                else:
                    break
        
        offset = 0
        
        #Scanning South-West Direction
        #X increases and Y decreases
        for i in range(moveX + 1, self.x):
            #Checks that Y is not out of bounds
            if (moveY - offset - 1 >= 0):
                if self.grid[i][moveY - offset - 1] == logo:
                    counterNE += 1
                    offset += 1
                else:
                    break
        
        offset = 0
        
        #Scanning North-West Direction
        #X decreases, Y decreases
        for i in range(0, moveX + 1):
            #Checks that X and Y are not out of bounds
            if (moveY - offset - 1 >= 0 and moveX - i - 1 >= 0):
                if self.grid[moveX - i - 1][moveY - offset - 1] == logo:
                    counterNW += 1
                    offset += 1
                else:
                    break
        
        offset = 0
        
        #Scanning South-East Direction (INCLUSIVE OF THE MOVE THE PLAYER JUST MADE)
        #X increases and Y increases
        for i in range(moveX, self.x):
            #Checks that Y is not out of bounds
            if (moveY + offset < self.y):
                if self.grid[i][moveY + offset] == logo:
                    counterNW += 1
                    offset += 1
                else:
                    break
        
        #If either counter is greater than or equal to the winning condition
        if (counterNW >= self.winLen or counterNE >= self.winLen):
            return True
        else:
            return False
    
    
    def gameOver(self, moveX, moveY, logo):
        '''
        Determines whether the game is over because of a Horizontal Win, Vertical Win,
        or Diagonal Win, or if the grid is full and there has been a tie.
        Args:
            moveX: the X coordinate of the move
            moveY: the Y coordinate of the move
            logo: player symbol
        Returns:
            True if a winner exists
            False if there is no winner
            "tie" if there has been a tie
        '''
        #Checks if a a player won horizontally, vertically, or diagonally
        winnerExists = (self.checkHorizontalWin(moveX, moveY, logo) or self.checkVerticalWin(moveX, moveY, logo) or self.checkDiagonalWin(moveX, moveY, logo))
        
        #By default, we assume the grid is fully occupied
        fullGrid = True
        
        #if a winner exists
        if winnerExists:
            return True
        else:
            #Checks if the grid is full (no available moves)
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    #If an empty spot still exists on the grid
                    if self.grid[i][j] == " . ":
                        #Set fullGrid to be false
                        fullGrid = False
            
            #If grid is indeed full
            if fullGrid:
                return "tie"
            #If grid is not full, and there is no winner
            else:
                return False
            
    