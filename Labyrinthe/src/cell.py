#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:mod:`Cell` module

:author: `Aya LAKEHAL, Stevenson PATHER, Johanna PULULU`

:date:  2018, November 

"""

class CellError(Exception):
    """
    Exception used by the method ``__init__`` of class :class:`Cell`.
    """
    def __init__(self, msg):
        self.message = msg
        
class Cell():
    """
    :param x: the position in x of the cell
    :param y: the position in y of the cell
    :type x: int
    :type y: int
    
    :build: a new cell with a x and y assigned position in the maze grid
    
    :UC: x and y must be positive integers
    
    :raise: :class:`CellError` if UC is not respected
    
    :Examples:
    
    >>> cel = Cell(0,0)
    >>> type(cel) == Cell
    True
    
    >>> cel = Cell(1.5,2.0)
    Traceback (most recent call last):
      ...
    CellError: x and y must be a positive integers
    >>> cel = Cell(1,2.0)
    Traceback (most recent call last):
      ...
    CellError: x and y must be a positive integers
    >>> cel = Cell(-1,0)
    Traceback (most recent call last):
      ...
    CellError: x and y must be a positive integers
    >>> cel = Cell(0,-1)
    Traceback (most recent call last):
      ...
    CellError: x and y must be a positive integers
    """
    def __init__(self, x, y):
        """
        We give to self as its parameters its position (x, y),
        respectively for the width and the height position in the maze grid.
        Her have four walls (top, left, right, bottom) who can be removed.
                
        :return: the self cell of a maze grid.
        :rtype: Cell
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(1,2)
        >>> cel.get_x()
        1
        >>> cel.get_y()
        2
        >>> cel.all_walls()
        True
        >>> cel.visited()
        False
        """
        if type(x) == int and x >= 0 and type(y) == int and y >= 0:
            self.__x = x
            self.__y = y
        else:
            raise CellError("x and y must be a positive integers")
        
        self.init_walls()
        self.__visited = False
        self.__in_path = False
        
    def get_x(self):
        """
        :return: the position in x of self in the maze grid
        :rtype: int
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,1)
        >>> cel.get_x()
        0
        """
        return self.__x
    
    def get_y(self):
        """
        :return: the position in y of self in the maze grid
        :rtype: int
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,1)
        >>> cel.get_y()
        1
        """
        return self.__y
    
    def get_pos(self):
        """
        :return: the position in (x, y) of self in the maze grid
                 using the the two previous methods get_x and get_y.
        :rtype: tuple
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,1)
        >>> cel.get_pos()
        (0, 1)
        """
        return (self.get_x(), self.get_y())
    
    def init_walls(self):
        """
        :return: None
        :side effect: create the four walls of the self :
        
                      - the top wall
                      - the bot wall
                      - the left wall
                      - the right wall
                      
                      True state is when the wall is presente, else False.
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.top_wall
        True
        
        >>> cel.bot_wall
        True
        
        >>> cel.left_wall
        True
        
        >>> cel.right_wall
        True
        """
        self.top_wall = True
        self.bot_wall = True
        self.left_wall = True
        self.right_wall = True
        
    def remove_wall(self, direction):
        """
        :return: None
        :side effect: modify the state of the presence of the wall to False, of self
                      in the direction give in parameter.
                      
                      possible direction :
                      
                      - "left" to remove the left wall
                      - "right" to remove the right wall
                      - "top" to remove the top wall
                      - "bot" to remove the bottom wall
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.remove_wall("right")
        >>> cel.right_wall == False
        True
        >>> cel.removed_wall()
        ['R']
        """
        if direction == "left":
            self.left_wall = False
        elif direction == "right":
            self.right_wall = False
        elif direction == "top":
            self.top_wall = False
        elif direction == "bot":
            self.bot_wall = False
            
    def removed_wall(self):
        """
        :return: a list that containing the first letter of the direction
                 for which the self wall(s) is removed. If self has all its walls
                 that return an empty list.
                 
        :rtype: list
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.removed_wall()
        []
        
        >>> cel.remove_wall("right")
        >>> cel.removed_wall()
        ['R']
        
        >>> cel.remove_wall("left")
        >>> cel.removed_wall()
        ['L', 'R']
        """
        l_removed_wall = []
        if not self.top_wall:
            l_removed_wall.append("T")
        if not self.bot_wall:
            l_removed_wall.append("B")
        if not self.left_wall:
            l_removed_wall.append("L")
        if not self.right_wall:
            l_removed_wall.append("R")
        return l_removed_wall

    def all_walls(self):
        """
        :return: True if self has all of his walls, False otherwise
                 
        :rtype: bool
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.all_walls()
        True
        
        >>> cel.remove_wall("right")
        >>> cel.all_walls()
        False
        """
        return self.top_wall and self.bot_wall and self.left_wall and self.right_wall
    
    def visited(self):
        """
        :return: True if self was visited (by a function in `Maze` class), False otherwise.
        :rtype: bool
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.visited()
        False
        """
        return self.__visited
    
    def get_visited(self):
        """
        :return: None
        :side effect: modify the state of the visit of self to True
        
        :UC: none
        
        :Examples:
        
        >>> cel = Cell(0,0)
        >>> cel.visited()
        False
        
        >>> cel.get_visited()
        >>> cel.visited()
        True
        """
        self.__visited = True
        
    def __repr__(self):
        """
        :return: external representation of the self cell:
                 position (x,y) of the cell
                 
        :rtype: Cell
        
        :UC: none
        
        >>> cell = Cell(0,0)
        >>> cell
        (0, 0)
        """
        return str(self.get_pos())
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)