===========
Project log
===========

.. topic:: Réalisé par

	* Aya LAKEHAL
	* Stevenson PATHER
	* Johanna PULULU
	
Journal de bord du projet d'Algorithmne et de Programmation 2. 

Vous retrouvez ici nos objectifs visés au début des différentes semaines ainsi que les bilans de celles-ci.

:note: l'ordre dans lequel les prénoms des auteurs du projet sont disposés n'a pas d'importances.
	
Semaine du 29 Octobre au 21 Novembre
====================================

Objectifs
---------

Notre objectif durant cette semaine est d'avancer au maximum pour pouvoir prendre du temps pour l'interface graphique avec le module tkinter par la suite.

Bilan
-----

Travail effectué :

	 - Classe :class:`cell` : section :
	 
				- Position de la cellule
				- Murs de la cellule

	 - Classe :class:`Maze` : section :	
	 
				- Dimension du labyrinthe
				- Path et grille du labyrinthe
				- Cellules du labyrinthe
				- Affichage en format texte du labyrinthe (__str__)
				- la fonction build_path
				
	 Remarque : concernant la classe :class:`Stack`, n'étant pas les auteurs du fichier Stack.py nous ne l'avons pas retoucher c'est pourquoi il ne sera pas mentionner de travaux effectués sur le fichier.

Semaine du 15 au 21 Novembre
============================

Objectifs
---------

	 - Résoudre le build_path du labyrinthe :

		 Le mur de la cellule où l'on se trouve, dans la direction choisi au hasard s'enlève correctement. Mais le mur entre la cellule où l'on se trouve et celle dans laquelle on va se diriger ne s'enlève pas.

	 - Faire la section "Construction du labyrinthe et recherche de sa sortie"

	 - Compléter cell.rst

	 - Compléter Maze.rst

Bilan
-----

	 - le soucis rencontré avait pour source des confusions dans les variables de directions T, B, R et L :
	 
		Avant :	T = (-1, 0), B = (1, 0), R = (0, 1), L = (0, -1)
		
		Après : T = (0, -1), B = (0, 1), R = (1, 0), L = (-1, 0)
		
		Respectivement T, B, R et L pour Top, Bottom, Right et Left.
				
	 - La fonction build_path de la section de construction étant déjà faîte la semaine d'avant. Nous avons donc réfléchit aux différentes méthodes possibles qui existent
	   pour pouvoir sortir d'un labyrinthe donc trouver sa sortie. Nous avons en cherchant trouvé l'algorithmne de Pledge. Mais après quelques tentatives d'applications
	   de cet algorithmne à notre projet. Nous avons abandonnés cette méthode.
	   Par la suite nous nous sommes rendus compte qu'une fonction récursive non terminale était possible et facilement applicable avec les outils dont nous disposons dans nos classes cell et Maze.
	   
	   Remarque : Un défaut est cependant notable dans ce que retourne find_exit : elle renvoie le chemin qu'a empreintée cette fonction avant d'arriver à la sortie (cellule de fin). Y compris les chemins qui mènent à un "cul-de-sac".
	   Même chose pour la fonction build_path qui va ajouter dans self.__path toutes les cellules qu'elle rencontre.
	   Une amélioration pourrait être de n'avoir que le chemin direct menant à la sortie.
				  
	 - Concernant les fichiers cell.rst et Maze.rst. Nous avons complétés ces fichiers avec les différentes méthodes de chacunes des classes mais sans écrire de descriptions ou d'informations complétementaires.
	   
Semaine du 22 au 28 Novembre
============================

Objectifs
---------

	 - Faire in_file et build_from_file

	 - Faire la doctest
	 
	 - Améliorer la fonction find_exit pour obtenir le chemin de sortie sans les culs-de-sacs (voir bilan semaine dernière) et le stocker dans directement dans self.__path

Bilan
-----
	 - La classe Maze est entièrement finie
	 
	 - Les doctests sont faîtes sauf pour les exemples de build_from_file et build in_file
	 
	 - Nous avons modifier certaines choses dans la fonction find_path et find_exit pour obtenir directement le chemin de sortie sans les culs-de-sacs. Cela fonctionne mieux mais dans un très grand nombre
	   de cas mais il y a encore des améliorations possibles à apporter. Par exemple dans certains cas nous avons la première cellule d'un chemin cul-de-sac qui est tout de même présente dans le chemin de sortie.
	   
Semaine du 29 Novembre au 05 Décembre
=====================================

Objectifs
---------

	 - Finir la doctest de Maze.py
	   
	 - Terminer les modifications sur find_path et find_exit pour n'avoir que le chemin direct vers la sortie
	 
	 - Vérifier les fichiers rst de Maze et cell
	 
	 - Se pencher sur l'utilisation de tkinter (graphicalmain.py)
	 
Bilan
-----

	 - La doctest de Maze est finie
	 
	 - Les modifications apportées ont finalement portées leurs fruits. Nous sommes arrivés à obtenir directement le chemin menant à la sortie des labyrinthes, sans les culs-de-sacs.
	 
	 - Nous avons donc un aperçu du rendu final (sans l'interface graphique) en cette fin de semaine. Nous devons encore essayer de trouver une solution pour mettre sur le fichier rst les fonctions dîtes "Inner function", les fonctions dans une fonction.
	   Ainsi que trouver le moyen de pouvoir faire leurs exemples dans les doctests.
	   
	 - Nous avons commencer à regarder le module tkinter pour préparer la dernière semaine.
	 
Semaine du 06 au 12 Décembre
============================

Objectifs
---------
		
	 - Trouver un moyen de faire des exemples pour les fonctions dans une fonction. Ainsi qu'afficher leurs doctests dans le fichier rst.
	 
	 - Relire les fichiers en entier une fois de plus pour corriger d'eventuelles erreurs de frappes dans la doc. 
	 
	 - Faire une interface graphique tkinter
	 
Bilan
-----


