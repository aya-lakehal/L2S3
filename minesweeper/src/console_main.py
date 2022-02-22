#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:mod:`console_main` module

:date:  2018, October

module to play the minesweeper's game : cmd version
"""

from minesweeper import *
import sys
    
def minesweeper_game(width=30, height=20, nbombs=99):
    """
    Fucntion that run a minesweeper game party
    
    :param width: width of the game grid
    :param height: height of the game grid
    :param nbombs: number of mine(s) in the game
    :type width: int
    :type height: int
    :type nbombs: int
    :UC: nbombs <= width * height
    """
    #I did not put an assert here for the UC nbombs <= width * height, because this is already present in minesweeper module.
    #I modified the formatting of the grid when the width is strictly greater than ten.
    #This one requires larger boxes because of the size of the two-digit numbers.
    #Personally on my screen of resolution 1920x1080 I can display in width 39 boxes maximum.
    #A screenshot of the rendering is available in the image folder and is named minesweeper_39x39.png.
    #The layout requested in this pratical work is fully respected if the width is strictly less than 10.
    
    def x_width(width=width):
        """
        Function that returns the str line that contains the number of x-coordinate which are separated by the right number of space character.
        
        :param width: width of the game grid
        :type width: int
        :return: the str that contains the number of x-coordinate
        :rtype: *str*
        :UC: none
        """
        l_w = []
        for w in range(width):
            l_w.append(str(w))
        if width > 10:
            x_width = "     "
            for e in l_w:
                if int(e) >= 9:
                    x_width += e+"    "
                else:
                    x_width += e+"     "
        else:
            x_width = "    "
            for e in l_w:
                x_width += e+"   "
        return(x_width+"\n")
    
    def spacing_line(width=width):
        """
        Function that returns the str spacing line "+---+" beetween the cells line. The size is according to the width of the game grid.
        
        :param width: width of the game grid
        :type width: int
        :return: the str spacing line
        :rtype: *str*
        :UC: none
        
        """
        if width > 10:
            spacing = "+-----"
        else:
            spacing = "+---"
        line = " "
        for i in range(width):
            line += spacing
        return(line+"+\n")
        
    def cell_line(line_number, width=width, height=height):
        """
        Function that returns the str line who contains the cells of the game.
        
        :param line_number: corresponds to the y-coordinate in other words the number of the line in the game grid
        :param width: width of the game grid
        :param height: height of the game grid
        :type line_number: int
        :type width: int
        :type height: int
        :return: str line who contains the cells of the game
        :UC: none
        
        """
        n_line = str(line_number)+"|"
        if width > 10:
            for x_cell in range(width):
                n_line += "  "+game.get_cell(x_cell,line_number).__str__()+"  |"
        else:
            for x_cell in range(width):
                n_line += " "+game.get_cell(x_cell,line_number).__str__()+" |"
        return(n_line+"\n")
    
    def print_grid():
        """
        Procedure that uses x_width, spacing_line and cell_line functions in order to print properly
        the grid of game.
        
        :UC: none
        """
        str_grid = x_width()
        if height > 10:
            for y_grid in range(height):
                if y_grid >= 10:
                    str_grid += (" "+spacing_line()+cell_line(y_grid))
                else:
                    str_grid += (" "+spacing_line()+" "+cell_line(y_grid))
            str_grid += " "+spacing_line()
        else:
            for y_grid in range(height):
                str_grid += (spacing_line()+cell_line(y_grid))
            str_grid += spacing_line()
        print(str_grid)
    
    def invalid_play():
        """
        Procedure that prints the instruction for having a valid play text
        
        :UC: none
        """
        print("                                                                     \n"
              "*********************************************************************\n"
              "*                       Minesweeper Assistance                      *\n"       
              "*********************************************************************\n"
              "*    You must write like this : x,y,C (C=(R)eveal,(S)et,(U)nset)    *\n"
              "*                                                                   *\n"
              "*    For example if you want (R)eveal the case x = 0 and y = 1      *\n"
              "*    You have to write this : 0,1,R                                 *\n"
              "*    Be sure that 0 <= x < width and 0 <= y < height                *\n"
              "*********************************************************************")
        
    def already(x,y,C):
        """
        Procedure that prints that the issue of the cell who was already played for the same action, or for a cell who has no flag
        and the player want to move the flag that does not exist on the cell.
        
        :UC: none
        """
        if C == "R":
            print("                                               \n"
                  "***********************************************\n"
                  "*           Minesweeper Assistance            *\n"
                  "***********************************************\n"
                  "*                                             *\n"
                  "*    The cell (x={0},y={1}) is already reaveled   *\n"
                  "*    Please play another one                  *\n"
                  "*                                             *\n"
                  "***********************************************\n".format(x,y))
        elif C == "S":
            print("                                               \n"
                  "***********************************************\n"
                  "*           Minesweeper Assistance            *\n"
                  "***********************************************\n"
                  "*                                             *\n"
                  "*    The cell (x={0},y={1}) has already a flag    *\n"
                  "*    Please play something other              *\n"
                  "*                                             *\n"
                  "***********************************************\n".format(x,y))
        else:
            print("                                               \n"
                  "***********************************************\n"
                  "*           Minesweeper Assistance            *\n"
                  "***********************************************\n"
                  "*                                             *\n"
                  "*    The cell (x={0},y={1}) has already no flag   *\n"
                  "*    Please play something other              *\n"
                  "*                                             *\n"
                  "***********************************************\n".format(x,y))
        
    game = Minesweeper(width, height, nbombs)
    print_grid()
    while game.get_state() == GameState.unfinished:
        play = input("Your play x,y,C (C=(R)eveal,(S)et,(U)nset): ")
        l_play = play.split(",")
        #I use try and except in order not to lose the game. Because if the player make a mistake on his answer of play
        #the AssertionError (or other errors) will make shutdown the program and the game party will be lost.
        try:
            if len(l_play) == 3 and l_play[2] in ("R", "S", "U"):
                x = int(l_play[0])
                y = int(l_play[1])
                C = l_play[2]
                if C == "R" and not game.get_cell(x,y).is_revealed():
                    game.reveal_all_cells_from(x,y)
                    print_grid()
                elif C == "S" and not game.get_cell(x,y).is_hypothetic():
                    game.get_cell(x,y).set_hypothetic()
                    print_grid()
                elif C == "U" and game.get_cell(x,y).is_hypothetic():
                    game.get_cell(x,y).unset_hypothetic()
                    print_grid()
                else:
                    already(x,y,C)
            else:
                invalid_play()
        except:
            invalid_play()
        game.check_the_win()
        
    if game.get_state() == GameState.losing:
        print("You lose!")
    else:
        print("You win!")
                
if __name__ == '__main__':
    if len(sys.argv) == 4:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        nbombs = int(sys.argv[3])
        minesweeper_game(width,height,nbombs)
    elif len(sys.argv) > 1:
        print("                                           \n"
              "*******************************************\n"
              "*         Minesweeper Assistance          *\n"
              "*******************************************\n"
              "*  Arguments given must be in the order : *\n"
              "*                                         *\n"
              "*     - The width                         *\n"
              "*     - The height                        *\n"
              "*     - The desired number of mine(s)     *\n"
              "*******************************************\n")
    else:
        minesweeper_game()
