=========================
:mod:`minesweeper` module
=========================

Ce module définit des classes et fonctions auxiliaires pour gérer le plateau du jeu de démineur.


Class description
=================

Une classe pour définir un type énuméré pour l'état du jeu.

La classe :class:`GameState`
----------------------------

.. autoclass:: minesweeper.GameState

Les trois états possibles du jeu : gagnant (winning), perdant (losing), ou inachevé (unfinished) sont décrits par trois attributs de mêmes noms.
			   
La classe :class:`Minesweeper`
------------------------------   

.. autoclass:: minesweeper.Minesweeper

Méthodes
~~~~~~~~

.. automethod:: minesweeper.Minesweeper.get_grid

.. automethod:: minesweeper.Minesweeper.get_width

.. automethod:: minesweeper.Minesweeper.get_height

.. automethod:: minesweeper.Minesweeper.get_nbombs
								
.. automethod:: minesweeper.Minesweeper.get_state

.. automethod:: minesweeper.Minesweeper.extend_zero_reveal

.. automethod:: minesweeper.Minesweeper.reveal_all_cells_from

.. automethod:: minesweeper.Minesweeper.check_the_win

Special method
~~~~~~~~~~~~~~

.. automethod:: minesweeper.Minesweeper.__init__


								
Fonction auxiliaire
===================

.. autofunction:: minesweeper.neighborhood

.. autofunction:: minesweeper.create_grid
