'''
Recevoir en entrée une configuration en une chaîne de caractère,
Par exemple :“8, 3”  pour 8 disques et 3 tours.
'''
# ------------VERSION 1------------------------------
start="8,3"
# Assignation du premier caractère à la variable disque
total_disques = start[0]
# Assignation du troisième caractère à la variable tour
total_tours = start[2]

# # -------------VERSION 2------------------------------- 
# total_disques=input("Choisissez un nombre de disque :")
# total_tours=input("Choisissez un nombre de tour :")
# start=f"{total_tours},{total_disques}"
# print(start)





'''
AU DEPART, IL Y A LES DISQUES, LES TOURS, TOUS LES DISQUES SONT SUR LA TOUR DE GAUCHE 
'''
disques = [i+1 for i in range(int(total_disques))]
# print(disques)

tours = [0 for i in range(int(total_tours))]
tours[0]=len(disques)

jeux = [tours[0],tours[1],tours[2]]
print(jeux)



'''déplacement'''

# for d in disques:
tours[0]-=1
tours[1]+=1

print(jeux)



'''
Afficher dans le terminal la liste des coups à jouer :
1 -> 3 : déplacer un disque du bâtonnet 1 au bâtonnet 3
1 -> 4 : déplacer un disque du bâtonnet 1 au bâtonnet 4
...
'''
