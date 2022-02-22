#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:mod:`Maze` module

:date:  2018, November 

"""
import sys 
from random import choice
from cell import *
from stack import *

T = (0, -1)
B = (0, 1)
R = (1, 0)
L = (-1, 0)

class MazeError(Exception):
    """
    Exception used by the methods:
        * ``__init__``
        * ``get_cell``
        * ``neigh_cell``
        * ``in_file``
        * ``build_from_file``
        
        of class :class:`Maze`.
    """
    def __init__(self, msg):
        self.message = msg

class Maze():
    """
    :param width: the width of the self maze
    :param height: the height of the self maze
    :type width: int
    :type height: int
    
    :build: a new maze structure with a width and height given in parameters
    
    :UC: the width and height must be positive integers
    
    :raise: :class:`MazeError` if UC is not respected
    
    :Examples:
    
    # Asnwer to the first job requested : Hand-made construction of a given size maze
    
    >>> laby = Maze(2,2)
    
    # Creation of the grid that's containing the cells of maze
    
    >>> laby.create_grid()
    
    # build a way to explore and to exit the maze
    
    >>> laby.get_cell((0,0)).remove_wall("bot") # == laby.get_cell((0,0)).bot_wall = False
    >>> laby.get_cell((0,1)).remove_wall("top") # == laby.get_cell((0,0)).top_wall = False
    >>> laby.get_cell((0,1)).remove_wall("right") # == laby.get_cell((0,0)).right_wall = False
    >>> laby.get_cell((1,1)).remove_wall("left") # == laby.get_cell((0,0)).left_wall = False
    
    # Verify the result by displaying the obtained maze
    
    >>> print(laby)
    +-+-+
    | | |
    + +-+
    |   |
    +-+-+
    
    >>> laby = Maze(-2,2)
    Traceback (most recent call last):
     ...
    MazeError: width and height must be a positive integers
    >>> laby = Maze(2,-2)
    Traceback (most recent call last):
     ...
    MazeError: width and height must be a positive integers
    >>> laby = Maze(2.5,2)
    Traceback (most recent call last):
     ...
    MazeError: width and height must be a positive integers
    >>> laby = Maze(2,2.5)
    Traceback (most recent call last):
     ...
    MazeError: width and height must be a positive integers
    """
    def __init__(self, width, height):
        """
        We give to self as its parameters his width and height.
        We create an empty dictionnary for the cell grid, an empty list for the path to exit
        and None value variable method named exit.
        
        :return: the self maze.
        :rtype: Maze
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.get_width()
        2
        >>> laby.get_height()
        2
        >>> laby.get_grid()
        {}
        >>> laby.get_path()
        []
        >>> laby.can_exit() == None
        True
        """
        if type(width) == int and type(height) == int and width >= 0 and height >= 0:
            self.__w = width
            self.__h = height
        else:
            raise MazeError("width and height must be a positive integers")
        
        self.__grid = {}
        self.__path = []
        self.__exit = None
        
    def get_width(self):
        """
        :return: the width of self maze
        :rtype: int
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,4)
        >>> laby.get_width()
        2
        """
        return self.__w
    
    def get_height(self):
        """
        :return: the height of self maze
        :rtype: int
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,4)
        >>> laby.get_height()
        4
        """
        return self.__h
        
    def get_grid(self):
        """
        :return: the grid of self maze
        :rtype: dict
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.get_grid()
        {}
        
        >>> laby.create_grid()
        >>> laby.get_grid()
        {(0, 0): (0, 0), (1, 0): (1, 0), (0, 1): (0, 1), (1, 1): (1, 1)}
        """
        return self.__grid
    
    def create_grid(self):
        """
        :return: None
        :side effect: create all cells of self maze in the grid dictionnary
                      with a total of width*height cells
                      
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> laby.get_grid()
        {(0, 0): (0, 0), (1, 0): (1, 0), (0, 1): (0, 1), (1, 1): (1, 1)}
        
        >>> cell = (0,0)
        >>> type(cell)
        <class 'tuple'>
        >>> type(laby.get_grid()[cell]) == Cell
        True
        """
        w = self.get_width()
        h = self.get_height()
        for y in range(w):
            for x in range(h):
                self.get_grid()[(x,y)] = Cell(x,y)
        self.start = self.get_grid()[(0,0)]
        self.end = self.get_grid()[(w-1,h-1)]
    
    def get_cell(self, pos):
        """
        :param pos: correspond to the tuple of the position (x,y) of the cell sought
        :type pos: tuple
        
        :return: the cell sought in the position (x,y)
        :rtype: Cell
        
        :UC: type(pos) == tuple and pos must like (x,y) with x and y positive integers
             0 <= x < width of self maze and 0 <= y < height of self maze
             
        :raise: :class:`MazeError` if UC is not respected
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> pos = (0,0)
        >>> type(pos) == tuple
        True
        >>> laby.get_cell(pos)
        (0, 0)
        >>> type(laby.get_cell(pos)) == Cell
        True
        
        >>> pos = (-1,-1)
        >>> laby.get_cell(pos)
        Traceback (most recent call last):
          ...
        MazeError: The argument must be a tuple like this (x,y):
            -   0 <= x < width of the maze
            -   0 <= y < hegiht of the maze
        >>> pos = [0,0]
        >>> laby.get_cell(pos)
        Traceback (most recent call last):
          ...
        MazeError: The argument must be a tuple like this (x,y):
            -   0 <= x < width of the maze
            -   0 <= y < hegiht of the maze
        """
        if type(pos) == tuple and 0 <= pos[0] < self.get_width() and 0 <= pos[1] < self.get_height():
            return self.get_grid()[pos]
        else:
            raise MazeError("The argument must be a tuple like this (x,y):\n"
                            "    -   0 <= x < width of the maze\n"
                            "    -   0 <= y < hegiht of the maze")
        
    def neigh_cell(self, cell, option="build"):
        """
        :param cell: the cell for wich we want the neighboring cell(s)
        :param option: (default value "build") purpose of use indicator of the function
        :type cell: Cell
        :type option: str
        
        :return: * if option == "build" : return a list that's containing tuples
                                          who containe in first the neighboring cell
                                          and in second the tuple of direction of the cell
                                          (check T,B,R and L variable)
                                        
                 * if option == "find"  : return a list that's containing all of
                                          the avaible neighboring cell(s). In other words
                                          all of cells that not have walls between them.
                                        
        :rtype: list
        
        :UC: type(option) == str and option must be "build" or "find"
        
        :raise: :class:`MazeError` if UC is not respected
        
        :Examples:
        
        >>> laby = Maze(3,3)
        >>> laby.create_grid()
        >>> cell = laby.get_cell((2,2))
        >>> example = laby.neigh_cell(cell)
        >>> example
        [((2, 1), (0, -1)), ((1, 2), (-1, 0))]
        
        >>> type(example[0][0])
        <class 'cell.Cell'>
        >>> type(example[0][1])
        <class 'tuple'>
        
        >>> cell = laby.get_cell((1,1))
        >>> laby.neigh_cell(cell)
        [((1, 0), (0, -1)), ((1, 2), (0, 1)), ((2, 1), (1, 0)), ((0, 1), (-1, 0))]
        """
        if option in ("build", "find"):
            directions = [T, B, R, L]
            str_directions = ["T", "B", "R", "L"]
            l_neigh = []
            i = 0
            for e in directions:
                d_x, d_y = cell.get_x() + e[0], cell.get_y() + e[1]
                if 0 <= d_x < self.get_width() and 0 <= d_y < self.get_height():
                    d_neigh_cell = self.get_cell((d_x, d_y))
                    if option == "build":
                        if d_neigh_cell.all_walls():
                            l_neigh.append((d_neigh_cell, e))
                    else:
                        if str_directions[i] in cell.removed_wall():
                            l_neigh.append(d_neigh_cell)
                i += 1
            return l_neigh
        else:
            raise MazeError("the last parameter option (str) must be 'build' (default value) or 'find'")
    
    def get_path(self):
        """
        :return: the list of the path that the function build_path or find_exit.
                 else return the empty list of path.
                 
        :rtype: list
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.get_path()
        []
        
        >>> laby.create_grid()
        >>> cell = laby.get_cell((0,0))
        >>> laby.add_path(cell)
        >>> len(laby.get_path()) != 0
        True
        >>> laby.get_path()
        [(0, 0)]
        """
        return self.__path
    
    def add_path(self, cell):
        """
        :param cell: the cell that we want at add in the path
        :type cell: Cell
        
        :return: None
        :side effect: append in the path list the cell given as argument
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> cell = laby.get_cell((0,0))
        >>> laby.add_path(cell)
        >>> cell in laby.get_path()
        True
        """
        self.__path.append(cell)
        
    def remove_last_in_path(self):
        """
        :return: None
        :side effect: remove the last cell in the path list of self maze
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> cell = laby.get_cell((0,0))
        >>> laby.add_path(cell)
        >>> laby.get_path()
        [(0, 0)]
        
        >>> laby.remove_last_in_path()
        >>> laby.get_path()
        []
        """
        self.__path.pop()
        
    def clear_path(self):
        """
        :return: None
        :side effect: clear the path list at his initial state (an empty list)
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> cell = laby.get_cell((0,0))
        >>> laby.add_path(cell)
        >>> laby.get_path()
        [(0, 0)]
        
        >>> laby.clear_path()
        >>> laby.get_path()
        []
        """
        self.__path = []
        
    def build_path(self):
        """
        :return: None
        :side effect: build a perfect labyrinth, in other words a maze with only one path to exit
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> laby.find_exit()
        False
        
        >>> laby.build_path()
        >>> laby.find_exit() != False
        True
        """
        if self.get_path() != []:
            self.clear_path()
            
        w = self.get_width()
        h = self.get_height()
        self.create_grid()
        st = Stack()
        cell_pos = self.start
        view_cells = 1
        total_cells = w*h
        
        while view_cells < total_cells:
            neighboors = self.neigh_cell(cell_pos)
            if len(neighboors) > 0:
                neigh, direction = choice(neighboors)
                if direction == T:
                    self.get_cell(cell_pos.get_pos()).remove_wall("top")
                    self.get_cell(neigh.get_pos()).remove_wall("bot")
                elif direction == R:
                    self.get_cell(cell_pos.get_pos()).remove_wall("right")
                    self.get_cell(neigh.get_pos()).remove_wall("left")
                elif direction == B:
                    self.get_cell(cell_pos.get_pos()).remove_wall("bot")
                    self.get_cell(neigh.get_pos()).remove_wall("top")
                elif direction == L:
                    self.get_cell(cell_pos.get_pos()).remove_wall("left")
                    self.get_cell(neigh.get_pos()).remove_wall("right")
                st.push(cell_pos)
                cell_pos = neigh
                view_cells += 1
            else:
                cell_pos = st.pop()
        self.__exit = True
        
    def can_exit(self):
        """
        :return: the self.__exit value : - None if we don't know if there is an exit path
                                         - True if an exit path exists
                                         - False if there is no exit path
                                         
        :rtype: bool
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> laby.can_exit() # This returns None
        
        >>> laby.build_path()
        >>> laby.can_exit()
        True
        """
        return self.__exit
                
    def find_exit(self):
        """
        :return: the path (the list that containe the cells) to get out the maze
                 else return the method can_exit state (= False) if the maze don't have an exit path
                 
        :rtype: list or bool
        
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> laby.find_exit()
        False
        
        >>> laby.get_cell((0,0)).remove_wall("bot") 
        >>> laby.get_cell((0,1)).remove_wall("top")
        >>> laby.get_cell((0,1)).remove_wall("right")
        >>> laby.get_cell((1,1)).remove_wall("left")
        >>> laby.find_exit()
        [(0, 0), (0, 1), (1, 1)]
        >>> print(laby)
        +-+-+
        | | |
        + +-+
        |   |
        +-+-+
        
        >>> laby = Maze(3,3)
        >>> laby.create_grid()
        >>> laby.get_cell((0,0)).remove_wall("bot") 
        >>> laby.get_cell((0,1)).remove_wall("top")
        >>> laby.get_cell((0,1)).remove_wall("right")
        >>> laby.get_cell((1,1)).remove_wall("left")
        >>> laby.get_cell((2,2)).remove_wall("left")
        >>> laby.get_cell((2,2)).remove_wall("top")
        >>> laby.get_cell((1,2)).remove_wall("right")
        >>> laby.get_cell((2,1)).remove_wall("bot")
        >>> print(laby)
        +-+-+-+
        | | | |
        + +-+-+
        |   | |
        +-+-+ +
        | |   |
        +-+-+-+
        >>> laby.find_exit()
        False
        """
        ####################################################################
        def find_path(self, cell=None):
            """
            :param cell: (default value None) the current where we are in
                         the maze in order to find a path to exit
                         
            :param l: a list that containe the path traveled
            :type cell: Cell
            :type l: list
            
            :return: True if the self maze have an exit path
                     else return False
                     
            :rtype: bool
            
            :UC: none
            """
            if cell == None:
                cell = self.end
            if cell == self.start:
                self.__exit = True
                return True
            elif not cell.visited():
                cell.get_visited()
                avaible_neighboors = self.neigh_cell(cell,"find")
                if len(avaible_neighboors) > 0:
                    for cel in avaible_neighboors:
                        if find_path(self,cel):
                            self.add_path(cel)
                            return True
            else:
                return False
        ###################################################################
        if self.get_path() == []:
            if not self.start.all_walls() and not self.end.all_walls():
                if find_path(self):
                    self.add_path(self.end)
                    return self.get_path()
                else:
                    self.__exit = False
                    return self.can_exit()
            else:
                self.__exit = False
                return self.can_exit()
        else:
            return self.get_path()
    
    def __str__(self):
        """
        :return: the self maze in text format
        :rtype: str
                                
        :UC: none
        
        :Examples:
        
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> laby.get_cell((0,0)).remove_wall("bot") 
        >>> laby.get_cell((0,1)).remove_wall("top") 
        >>> laby.get_cell((0,1)).remove_wall("right") 
        >>> laby.get_cell((1,1)).remove_wall("left")  
        >>> print(laby)
        +-+-+
        | | |
        + +-+
        |   |
        +-+-+
        """
        w = self.get_width()
        h = self.get_height()
        #####################################################
        def FE_line_str(self):
            """
            :return: the first and the last line of the
                     self maze in text format in terms of
                     the width of theh maze
                    
            :rtype: str
            
            :UC: none
            """
            return("+-"*w+"+")
        
        def cell_line_str(self, line):
            """
            :param line: y for which we want to have
                         the cell line (with or without
                         their walls) in format text
                         
            :return: a str line with or without somes walls
                     in order to correspond to the y line
                     of the self maze
                     
            :UC: none
            """
            l_cell = []
            for cell in self.get_grid():
                if self.get_cell(cell).get_y() == line:
                    l_cell.append(self.get_cell(cell))
            cell_line = ""
            spacing_line_str = ""
            for cells in l_cell:
                if cells.left_wall:
                    cell_line += "| "
                else:
                    cell_line += "  "
                if cells.bot_wall:
                    spacing_line_str += "+-"
                else:
                    spacing_line_str += "+ "
            if line == self.get_height()-1:
                return(cell_line+"|")
            else:
                return(cell_line+"|\n"+spacing_line_str+"+")
        #####################################################
        laby_str = FE_line_str(self) + "\n"
        for i in range(h):
            laby_str += cell_line_str(self,i) + "\n"
        laby_str += FE_line_str(self)
        return(laby_str)
    
    def in_file(self, file):
        """
        :param file: the name of file where we want to write, save the maze in text format
        :type file: str
        
        :return: None
        :side effect: write in file the maze in text format
        
        :UC: file must be a str
        
        :raise: :class:`MazeError` if UC is not respected
        
        :Examples:
        
        >>> import os
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> print(laby)
        +-+-+
        | | |
        +-+-+
        | | |
        +-+-+    
        >>> laby.in_file("Maze_file")
        >>> laby_from_file = Maze.build_from_file("Maze_file")
        >>> print(laby_from_file)
        +-+-+
        | | |
        +-+-+
        | | |
        +-+-+
        >>> os.remove("Maze_file.txt") # in order to delete the created file before
        
        >>> laby.in_file(Maze_2_2)
        Traceback (most recent call last):
          ...
        NameError: name 'Maze_2_2' is not defined
        
        >>> laby.in_file(123)
        Traceback (most recent call last):
          ...
        MazeError: the type of the argument file must be str and like : 'Example_name'
        """
        if type(file) == str:
            laby = str(self.get_width()) + "\n" + str(self.get_height()) + "\n" + self.__str__()
            with open(file+".txt", 'w', encoding='utf_8') as sortie:
                sortie.write(laby)
        else:
            raise MazeError("the type of the argument file must be str and like : 'Example_name'")
    
    @staticmethod
    def build_from_file(file):
        """
        :return: the builded maze saved in the argument file in text format
        :rtype: Maze
        
        :UC: file must be a str
        
        :raise: :class:`MazeError` if UC is not respected
        
        :Examples:
        
        >>> import os
        >>> laby = Maze(2,2)
        >>> laby.create_grid()
        >>> print(laby)
        +-+-+
        | | |
        +-+-+
        | | |
        +-+-+
        >>> laby.in_file("Maze_file")
        
        >>> laby_from_file = Maze.build_from_file("Maze_file")
        >>> print(laby_from_file)
        +-+-+
        | | |
        +-+-+
        | | |
        +-+-+
        >>> os.remove("Maze_file.txt")
        
        >>> laby.build_from_file(Maze_2_2)
        Traceback (most recent call last):
          ...
        NameError: name 'Maze_2_2' is not defined
        
        >>> laby.build_from_file(123)
        Traceback (most recent call last):
          ...
        MazeError: the type of the argument file must be str and like : 'Example_name'
        """
        ########################################################################
        def sides_walls(maze, line, y):
            """
            :param maze: the name of the maze that we create from a file
            :param line: the str line in which we want to know which side walls
                         are present or not
            :param y: correspond to the position in y of the argv line
            :type maze: Maze
            :type line: str
            :param y: int
            
            :return: None
            :side effect: modify the state of presence of walls of cells in the
                          line y content in the maze grid
            
            :UC: none
            """
            width = maze.get_width()
            carac_cmp = 0
            x = 0
            while x < width:
                if line[:-1][carac_cmp] == " ":
                    maze.get_cell((x-1,y)).remove_wall("right")
                    maze.get_cell((x,y)).remove_wall("left")
                carac_cmp += 2
                x += 1
        def fronts_walls(maze, line, y):
            """
            :param maze: the name of the maze that we create from a file
            :param line: the str line in which we want to know which top
                         and bot walls are present or not
            :param y: correspond to the position in y of the argv line
            :type maze: Maze
            :type line: str
            :param y: int
            
            :return: None
            :side effect: modify the state of presence of top and bot walls
                          of cells in the line y content in the maze grid
            
            :UC: none
            """
            width = maze.get_width()
            carac_cmp = 1
            x = 0
            while x < (width):
                if line[:-1][carac_cmp] == " ":
                    maze.get_cell((x,y)).remove_wall("bot")
                    maze.get_cell((x,y+1)).remove_wall("top")
                carac_cmp += 2
                x += 1
        ########################################################################
        if type(file) == str:
            with open(file+".txt", "r") as enter:
                l_laby = enter.readlines()
            l_laby.reverse()
            width = int(l_laby.pop()[0])
            height = int(l_laby.pop()[0])
            l_laby.pop()
            maze = Maze(width, height)
            maze.create_grid()
            y = 0
            while y < height:
                sides_walls(maze,l_laby.pop(),y)
                fronts_walls(maze,l_laby.pop(),y)
                y += 1
            return maze
        else:
            raise MazeError("the type of the argument file must be str and like : 'Example_name'")

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    if len(sys.argv) == 3:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        laby = Maze(width,height)
        laby.build_path()
        print(laby)
