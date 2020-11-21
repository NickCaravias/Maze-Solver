"""
  Class Maze defines a general structure of a maze
  which consists of a two-dimensional array of characters.
  Each symbol on the maze represents eiehter a possible path
  or a blocker.
 
  Students need to complete this class
"""

import random     # random number generator

class Maze:

    def __init__( self, max_row = 12, max_sol = 12 ):
        """Create a maze"""
        self.MAXROW = max_row
        self.MAXCOL = max_sol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5
        
        self.theMaze = []
        
        
    
    def _gen_maze( self ): 
        
        """Generate a random maze based on probability"""
        local_maze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]
        

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    local_maze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    local_maze[ row ][ col ] = self.BLOCKER
                    
        self.theMaze = local_maze
        
        return self.theMaze
    
    def _gen_user_maze( self ): 
        
        """Generate a random maze based on probability for the user to look at"""
        in_file = open('mazeuser.dat')
        lines = in_file.read()
        
        point = '*'
        exclamation = '!'
        space = ' ' 
        slot = []
        self.arr = []

        for i in lines:
            
            if (i == space) or (i == point) or (i == exclamation):
                slot.append(i)
                
        
            else:
                self.arr.append(slot)
                slot = []
        
        self.theMaze = self.arr
    
    """Generate a string representation of the maze"""
    def __str__( self ):
        
        row = self.MAXCOL
        rowToPrint = '  '
        for i in range(row):
            
            if i < 10: 
                rowToPrint = rowToPrint + str(i)
            
            if i >= 10:
                i = int(repr(i)[-1])
                rowToPrint = rowToPrint + str(i)
                
        print(rowToPrint)
            
        
        string = ''
        counter = 0
        
        arr = self.theMaze
        for i in arr:
            for j in i:
                string = string + str(j)
            
            print(counter, string)
            counter += 1
            if counter >= 10:
                counter = int(repr(counter)[-1])
            string = ''
                    
            
        """Getter for column count"""
    def get_col_size( self ):
        
        return self.MAXCOL
    
    """Getter for row count"""
    def get_row_size( self ):
        return self.MAXROW

    
    """Reads the maze from a file"""
    def read_maze( self, file_name ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        in_file = open(file_name)
        lines = in_file.read()
        
        point = '*'
        space = ' ' 
        slot = []
        self.arr = [] #added self

        for i in lines:
            
            if (i == space) or (i == point):
                slot.append(i)
        
            else:
                self.arr.append(slot)
                slot = []
        
        self.theMaze = self.arr
        
        
    """
    Method to make ask the user to decide if they want to enter a file or 
    generate a randome one
    """
    def mazeDecision(self):
        
        #ask the user if they want to enter a file
        whatMaze = input('Enter the name of the maze file (press enter to randomly generate a maze): ')
        
        self.whatMaze = whatMaze
        
    
        #try-except to catch any entry that is not a valid file
        try:
            self.read_maze(whatMaze)
            
            
        except:
            print('There is no file with this name!\n\nRandomly generating maze\n\n')
            self._gen_maze()
        
       
    """Getter method for a copy of the maze"""
    def get_maze( self ):
        return self.local_maze
    
    
    """Return True if this cell is clear (pathway)."""
    def is_clear( self, row, col ):
        self.row = row
        self.col = col
        maze = self.theMaze
        cell = maze[row][col]
        clear = ' '
        result = False
        
        if cell == clear:
            result = True
            
        return result
            
        
    def is_in_maze( self, row, col ):
        """Return True if a cell is inside the maze."""
        
        
        
        """
        setter method for the value fo a cell in the maze
        Params
        row and col to find the cell
        the value to add to the call
            
        """
    def set_value(self, row, col, value):
        
        self.row = int(row)
        self.col = int(col)
        self.value = value 
        
        maze = self.theMaze
        
        maze[row][col] = value
        
        self.theMaze = maze
        
        

    def get_value( self, row, col):
        """Return the value of the current cell."""
        
        maze = self.theMaze
        
        value = maze[row][col]
        
        return value
    
    """ getter for the value to the right of the entered value"""
    def getRight(self, row, col):
        maze = self.theMaze
        col += 1
        
        value = maze[row][col]
        
        if value != '*':
            return True
        else:
            return False
       
    
    
    """ getter for the value to the left of the entered value"""
    def getLeft(self, row, col):
        maze = self.theMaze
        col -= 1
        
        value = maze[row][col]
        
        if value != '*':
            return True
        else:
            return False
    
    
    """ getter for the value above the entered value"""
    def getAbove(self, row, col):
        maze = self.theMaze
        row -= 1
        
        value = maze[row][col]
        
        if value != '*':
            return True
        else:
            return False
    
    
    """ getter for the value below the entered value"""
    def getBelow(self, row, col):
        maze = self.theMaze
        row += 1
        
        value = maze[row][col]
        
        ast = '*'
        if value == ast:
            return False
        else:
            return True
    




