#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:date:  2018, October

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: widthof the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    >>> neighborhood(0, 9, 10, 10)
    [(0, 8), (1, 8), (1, 9)]
    >>> neighborhood(9, 0, 10, 10)
    [(8, 0), (8, 1), (9, 1)]
    >>> neighborhood(4, 0, 10, 10)
    [(3, 0), (5, 0), (3, 1), (4, 1), (5, 1)]
    >>> neighborhood(9, 4, 10, 10)
    [(8, 3), (8, 4), (8, 5), (9, 3), (9, 5)]
    
    """
    assert 0 <= x < width, 'the first argument (x-coordinate) must be 0 <= x < width'
    assert 0 <= y < height, 'the second argument (y-coordinate) must be 0 <= y < height'
    width_1 = width-1
    height_1 = height-1
    if x == 0 and y == 0:
        return [(x,y+1),(x+1,y),(x+1,y+1)]
    elif x == 0 and y == height_1:
        return [(x,y-1),(x+1,y-1),(x+1,y)]
    elif x == 0:
        return [(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
    elif y == 0 and x == width_1:
        return [(x-1,y),(x-1,y+1),(x,y+1)]
    elif y == 0:
        return [(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    elif x == width_1 and y == height_1:
        return [(x-1,y-1),(x-1,y),(x,y-1)]
    elif x == width_1:
        return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1)]
    elif y == height_1:
        return [(x-1,y-1),(x-1,y),(x,y-1),(x+1,y-1),(x+1,y)]
    else:
        return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
    
def create_grid(width, height, nbombs):
    """
    Create a game grid of the size width*height and place randomly nbombs in the grid. 
        
    :param width: width of the game grid
    :param height: height of the game grid
    :param nbombs: number of bombs in the game grid
    :type width: int
    :type height: int
    :type nbombs: int
    :return: Return a dictionary that contains for key tuple of (x-coordinate, y-coordinate) associate for value the cell which corresponds to this coordinates.
    :rtype: dict
    :UC: none
    """
    grid = {}
    for w in range(width):
        for h in range(height):
            grid[(w,h)] = Cell()
    i = 0
    while i != nbombs:
        r_cell = (random.randint(0,width-1),random.randint(0,height-1))
        if not grid[r_cell].is_bomb():
            grid[r_cell].set_bomb()
            n_cell = neighborhood(r_cell[0], r_cell[1], width, height)
            for cel in n_cell:
                grid[cel].incr_number_of_bombs_in_neighborhood()
            i += 1
    return(grid)

class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished 
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    >>> 
    """
    
    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.  

        :param width: [optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20
        >>> game.get_height()
        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished 
        True
        """
        assert type(width) == int and type(height) == int, 'width and height must be integer'
        assert width > 0 and height > 0, 'width and height must be positive integer'
        assert nbombs <= width*height, 'nbombs must be <= width * height'
        self.__width = width
        self.__height = height
        self.__nbombs = nbombs
        self._gs = GameState(3)
        self.__grid = create_grid(width,height,nbombs)
    
    def get_grid(self):
        """
        :return: grid of the game
        :rtype: dict
        :UC: none
        """
        return self.__grid
        
    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.__height

    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
            """
        return self.__width
    
    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """
        return self.__nbombs

    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :rtype: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        assert 0 <= x < self.__width, 'the first argument (x-coordinate of self cell) must be 0 <= x < width of game'
        assert 0 <= y < self.__height, 'the second argument (y-coordinate of self cell) must be 0 <= y < height of game'
        return self.get_grid()[(x,y)]
        
    def get_state(self):
        """
        :return: the state of the game (winning, losing or unfinished)
        :rtype: GameState
        :UC: none
        """
        return self._gs
     
    def extend_zero_reveal(self, x, y):
        """
        Method who reveal all zero cells around the (x,y) cell until number of bombs in neighbordhood of the cells in neighbordhood of the cell in l_extend queue is > 0.
            
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
            
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        l_extend = [(x,y)]
        l_reveal = []
        added = True
        w = self.get_width()
        h = self.get_height()
        while added:
            added = False
            l_extend, l = [], l_extend
            for x, y in l:
                positions = neighborhood(x,y,w,h)
                for cel in positions:
                    if not self.get_cell(cel[0],cel[1]).is_bomb() and cel not in l_reveal:
                        l_reveal.append(cel)
                        if self.get_cell(cel[0],cel[1]).number_of_bombs_in_neighborhood() == 0:
                            l_extend.append(cel)
                            added = True
        for e in l_reveal:
            self.get_cell(e[0],e[1]).reveal()
        
    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game game from the initial cell (x,y).
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        assert 0 <= x < self.__width, 'the first argument (x-coordinate of self cell) must be 0 <= x < width of game'
        assert 0 <= y < self.__height, 'the second argument (y-coordinate of self cell) must be 0 <= y < height of game'
        if self.get_cell(x,y).is_bomb():
            self.get_cell(x,y).reveal()
            self._gs = GameState(2)
        elif self.get_cell(x,y).number_of_bombs_in_neighborhood() > 0:
            self.get_cell(x,y).reveal()
        else:
            self.get_cell(x,y).reveal()
            l = neighborhood(x,y,self.get_width(),self.get_height())
            for cells in l:
                self.extend_zero_reveal(cells[0],cells[1])
                
    def check_the_win(self):
        """
        Change the gamestate of the game if the game is win
        
        :UC: none
            
        """
        l_reveal_cell = []
        for cel in self.get_grid():
            if self.get_cell(cel[0],cel[1]).is_revealed():
                l_reveal_cell.append(cel)
        if len(l_reveal_cell) == (len(self.get_grid()) - (self.get_nbombs())):
            self._gs = GameState(1)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
