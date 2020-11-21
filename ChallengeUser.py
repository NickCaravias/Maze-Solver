#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSCI204 Data Structures and Algorithms
Professor Gutekunst

Class to let the user try to challenge the speed the algorithm can solve the maze

@author: nickcaravias
"""

import time
from maze import Maze 



class ChallengeUser(Maze):
    def __init__(self):
        self.solveMazeUser()
    
    
    """ Method to create maze for the user to solve and time the user"""
    def solveMazeUser(self):
        
        answer = input('Do you want to challenge the algorithm? (y/n): ' )
        
        if answer == 'y':
            m = Maze()
            
            
            t0 = time.time() #starts the timer for the user to solve
            m._gen_user_maze()
            m.__str__()
            
            #timer will stop once the user presses enter and the code can continue
            input('Press enter when you have solved the maze by tracing it with your mouse' ) 
            
            
            #finds the time by subtracting total time from start time
            t1 = time.time()
            total = t1-t0
            
            
            print('It took you')
            print(total, ' seconds to solve the maze')
            
            return




