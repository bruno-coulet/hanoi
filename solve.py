'''
Recevoir en entrée une configuration en une chaîne de caractère,
Par exemple :“8, 3”  pour 8 disques et 3 tours.
'''
# ------------VERSION 1------------------------------
start="8,3"
total_disques = int(start[0])
total_tours = int(start[2])

# # -------------VERSION 2------------------------------- 
# total_disques=input("Choisissez un nombre de disque :")
# total_tours=input("Choisissez un nombre de tour :")
# start=f"{total_tours},{total_disques}"
# print(start)



'''
au départ, il y a les disques et les tours.'''
disques = [i+1 for i in range(total_disques)]
print(f"list des disques : {disques}")
tours = [0 for i in range(total_tours)]

'''tous les disques sont sur la tour de gauche'''
tours[0]=len(disques)
print(f"list des tours en début du jeu: {tours}")
# tours = [[i for i in range(total_disques, 0, -1)], [], []]


jeux = [tours[0],tours[1],tours[2]]
# print(jeux)



'''déplacement'''

for d in range(total_disques):
    tours[0] = (tours[0])-1
    tours[1] = (tours[1])+1

print(jeux)



'''
Afficher dans le terminal la liste des coups à jouer :
1 -> 3 : déplacer un disque du bâtonnet 1 au bâtonnet 3
1 -> 4 : déplacer un disque du bâtonnet 1 au bâtonnet 4
...
'''
