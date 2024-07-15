## Hanoi Tower

### Un jeu de réflexion

Les Tours de Hanoi sont un jeu de réflexion.<br>

Le but du jeu est de déplacer des disques de diamètres différents empilés par ordre croissant d'une tour de départ à une tour d'arrivée en passant par une tour intermédiaire.<br>

Il n’est possible de bouger qu’un disque à la fois.<br>
Un disque ne peut être placé que sur un disque plus gros.<br>

L'objectif est de faire un minimum de déplacements.


### Outil de résolution

Le programme reçoit en entrée une configuration de partie à résoudre, sous la forme d’une chaîne de caractère. Par exemple :
“8, 3” pour une partie a 8 disques et 3 bâtonnets.
“172, 5” pour une partie a 172 disques et 5 bâtonnets.

Il affiche ensuite dans le terminal la liste des
coups à jouer.
1 -> 3 : déplacer un disque du bâtonnet 1 au bâtonnet 3
1 -> 4 : déplacer un disque du bâtonnet 1 au bâtonnet 4
3 -> 4 : déplacer un disque du bâtonnet 3 au bâtonnet 4

Il doit fournir la solution qui requiert le moins de
déplacements possibles à l’aide du principe de récursivité.

Afficher une interface graphique dans laquelle il est possible de jouer à la tour d’Hanoi, mais aussi de proposer une résolution rapide étape par étape.<br>

### Rendu

L’évaluation de ce projet se fera sur deux aspects :
1. Une présentation explicative du travail sous forme de diapositives.

2. Un repository github public nommé hanoi-tower, contenant les éléments
suivants:
a. Un script solve.py.
b. Un script main.py.
c. Un script graphics.py
d. Un fichier README.md présentant la problématique du projet, la solution
proposée et une conclusion sur votre travail.
