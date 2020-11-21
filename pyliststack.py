# Implementation of the Stack ADT using a Python list.
class Stack :
   # Creates an empty stack.
  def __init__( self ):
    self._the_items = list()
  
   # Returns True if the stack is empty or False otherwise.
  def is_empty( self ):
    return len( self ) == 0
  
   # Returns the number of items in the stack.
  def __len__ ( self ):
    return len( self._the_items ) 
    
   # Returns the top item on the stack without removing it.
  def peek( self ):
    assert not self.is_empty(), "Cannot peek at an empty stack"
    return self._the_items[-1]
       
   # Removes and returns the top item on the stack.
  def pop( self ):
    assert not self.is_empty(), "Cannot pop from an empty stack"
    return self._the_items.pop()
  
   # Push an item onto the top of the stack.
  def push( self, item ):
    self._the_items.append( item )
    
  def __str__( self ):
      print(self._the_items)
      

      
