'''
Reçoit en entrée une configuration en chaîne de caractère,
Par exemple :“8, 3”  pour 8 disques et 3 tours.
'''
# ------------VERSION 1------------------------------
start_string="5,3"

# Séparer la chaîne en utilisant la virgule comme délimiteur
parts = start_string.split(',')
# Assigner les valeurs aux variables
total_disks = int(parts[0])
total_towers = int(parts[1])


# # -------------VERSION 2------------------------------- 
# total_disks=input("Choisissez un nombre de disque :")
# total_towers=input("Choisissez un nombre de tour :")
# start=f"{total_towers},{total_disks}"
# print(start)



'''au départ, il y a les disks et les towers.'''
disks = [i+1 for i in range(total_disks)]
print(f"list des disks : {disks}")
towers = [0 for i in range(total_towers)]
print(f"list des towers: {towers}")



'''tous les disks sont sur la tour de gauche'''
towers[0]=disks
towers[1]=[]
towers[2]=[]