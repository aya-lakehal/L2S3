======================
:mod:`cell` module
======================

.. automodule:: cell
   :members: __doc__
   
Class :class:`CellError`
========================

.. autoclass:: cell.CellError

   
Class :class:`Cell`
===================

.. autoclass:: cell.Cell

Special methods
---------------

.. automethod:: Cell.__init__

.. automethod:: Cell.__repr__

Cell position
-------------

.. automethod:: Cell.get_x

.. automethod:: Cell.get_y

.. automethod:: Cell.get_pos

Walls of the cell
-----------------

.. automethod:: Cell.init_walls

.. automethod:: Cell.remove_wall

.. automethod:: Cell.removed_wall

.. automethod:: Cell.all_walls

Marking on the cell
-------------------

.. automethod:: Cell.visited

.. automethod:: Cell.get_visited
