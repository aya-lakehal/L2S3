======================
:mod:`Maze` module
======================

.. automodule:: Maze
   :members: __doc__

Class :class:`MazeError`
========================

.. autoclass:: Maze.MazeError


Class :class:`Maze`
===================

.. autoclass:: Maze.Maze


Special methods
---------------

.. automethod:: Maze.__init__

.. automethod:: Maze.__str__

Dimension of maze
-----------------

.. automethod:: Maze.get_width

.. automethod:: Maze.get_height

Grid of the maze
----------------

.. automethod:: Maze.create_grid

.. automethod:: Maze.get_grid

Maze cells
----------

.. automethod:: Maze.get_cell

.. automethod:: Maze.neigh_cell

Path of the maze
----------------

.. automethod:: Maze.get_path

.. automethod:: Maze.add_path

.. automethod:: Maze.remove_last_in_path


Construction of the maze and search for its exit
------------------------------------------------

.. automethod:: Maze.build_path

.. automethod:: Maze.can_exit

.. automethod:: Maze.find_exit


Saving to a file and building a maze from a text backup
-------------------------------------------------------

.. automethod:: Maze.in_file

.. automethod:: Maze.build_from_file