'''
Reçoit en entrée une configuration en chaîne de caractère,
Par exemple :“8, 3”  pour 8 disques et 3 tours.
'''
# ------------VERSION 1------------------------------
start_string="8,3"
#  8 discs
total_discs = int(start_string[0])
#  3 towers
total_towers = int(start_string[2])

# # -------------VERSION 2------------------------------- 
# total_discs=input("Choisissez un nombre de disque :")
# total_towers=input("Choisissez un nombre de tour :")
# start=f"{total_towers},{total_discs}"
# print(start)



'''au départ, il y a les discs et les towers.'''
discs = [i+1 for i in range(total_discs)]
print(f"list des discs : {discs}")
towers = [0 for i in range(total_towers)]
print(f"list des towers: {towers}")



'''tous les discs sont sur la tour de gauche'''
towers[0]=discs
towers[1]=[]
towers[2]=[]

print(f"Position des discs en début du jeu: {towers}")



game = [towers[0],towers[1],towers[2]]
# print(game)



'''déplacement'''
def move(source, destination):
    if towers[source]:
        moving=towers[source].pop(0)
        towers[destination].append(moving)

        print(f"Déplace un disque de la tour {source} à la tour {destination}")
    else:
        print(f"Erreur : la tour {source} est vide")


# Déplacement d'un disque de la tour 1 à la tour 2
move(0, 1)
print("Après avoir déplacé le disque :")
print(towers)




'''
Afficher dans le terminal la liste des coups à jouer :
1 -> 3 : déplacer un disque du bâtonnet 1 au bâtonnet 3
1 -> 4 : déplacer un disque du bâtonnet 1 au bâtonnet 4
...
'''
