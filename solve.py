'''
Recevoir en entrée une configuration en une chaîne de caractère,
Par exemple :“8, 3”
8 disques et 3 bâtonnets.
'''
# ------------VERSION 1------------------------------
start="8,3"
# Assignation du premier caractère à la variable disque
total_disques = start[0]
# Assignation du troisième caractère à la variable battonet
battonet = start[2]

# -------------VERSION 2------------------------------- 
# total_disques=input("Choisissez un nombre de disque :")
# battonet=input("Choisissez un nombre de battonet :")
# start=f"{battonet},{total_disques}"
# print(start)

disques = [i+1 for i in range(int(total_disques))]
print(disques)

'''
Afficher dans le terminal la liste des coups à jouer :
1 -> 3 : déplacer un disque du bâtonnet 1 au bâtonnet 3
1 -> 4 : déplacer un disque du bâtonnet 1 au bâtonnet 4
...
'''
