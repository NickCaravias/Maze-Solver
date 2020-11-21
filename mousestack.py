#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSCI204 Data Structures and Algorithms
Professor Gutekunst

Class to solve a 12x12 maze using stacks

@author: nickcaravias
"""
#import copy
from maze import Maze 
from pyliststack import Stack
import time

class Mouse(Maze):
    
    def __init__(self):
        super().__init__()
        
        self.mazeDecision()
        print('-------The Original Maze-------')
        
        self.__str__()
        
        self.askQuestions()
        self.solveMaze(self.theMaze, (self.startCol, self.startRow))
        
        
        
    """Method to ask the user for the start and end points in the maze"""
    def askQuestions(self):
        self.startRow = input('enter start row: ')
        self.startRow = int(self.startRow)
        
        self.startCol = input('enter start column: ')
        self.startCol = int(self.startCol)
        
        self.endRow = input('enter end row: ')
        self.endRow = int(self.endRow)
        
        self.endCol = input('enter end column: ')
        self.endCol = int(self.endCol)
        
        
    """Helper method to check if the point the stack can move to is valid"""
    def isValid(self, pair):
        maze = self.theMaze
        (col, row) = pair
        
        if (col < 0) or (row < 0) or (col >= 12)  or (row >= 12):
            return False
        return maze[row][col] == ' ' or maze[row][col] == 'Finish'
    
    
    """
    Method to solve the maze with a stack
    Params
        maze: the maze to be solves
        start: the start location of the maze
    """
    def solveMaze(self, maze, start):
        
        (col,row) = start
        
        #create an empty stack
        s = Stack()
        
        #push the start on the stack
        s.push((col,row))
        
        #sets the finish point to a unique cell to be found by the stack
        maze[self.endRow][self.endCol] = 'Finish'
        
        
        #starts timer for the algorithm
        t0 = time.time()
        
        #while the stack is not empty
        while not s.is_empty():
                   
            (col, row) = s.pop()
        
            #if the stack find the finish end the loop
            if maze[row][col] == 'Finish':
                
                print('\n\nThe Maze is solved!\n')
                maze[row][col] = '!'
                self.__stackToStr__(maze)
                
                
                #ends timer for the algorithm
                t1 = time.time()
                total = t1-t0
                print('\nThe algorithm solved the maze in: ')
                print(total, 'seconds\n')
                
                print('Were you able to beat the algorithm speed on a similar maze?')
                
                return
            
            
            #if the end of the maze is not found then explore the four ways to move
            if maze[row][col] == ' ':
                self.set_value(row, col, '!')
                
                if self.isValid((col+1, row)): 
                    s.push((col+1, row))
                    
                if self.isValid((col, row+1)): 
                    s.push((col, row+1))
                    
                if self.isValid((col-1, row)): 
                    s.push((col-1, row))
                    
                if self.isValid((col, row-1)): 
                    s.push((col, row-1))
        
        
    """ Helper method to convert the stack maze to a string representation"""
    def __stackToStr__(self, maze):
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
        
        arr = maze
        for i in arr:
            for j in i:
                string = string + str(j)
            
            print(counter, string)
            counter += 1
            if counter >= 10:
                counter = int(repr(counter)[-1])
            string = ''













