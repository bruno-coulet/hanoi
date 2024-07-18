'''
Reçoit en entrée une configuration en chaîne de caractère,
Par exemple :“8, 3”  pour 8 disques et 3 tours.
'''
# ------------VERSION 1------------------------------
start_string="5,3"
# Sépare la chaîne et convertir les valeurs en entiers
values = [int(x) for x in start_string.split(',')]

# Assigner les valeurs aux variables
disks, towers = values
# print(values)
# print(type(values))
# print("disks",type(disks),", towers",type(towers))



# # -------------VERSION 2------------------------------- 
# total_disks=input("Choisissez un nombre de disque :")
# total_towers=input("Choisissez un nombre de tour :")
# start=f"{total_towers},{total_disks}"
# print(start)



'''au départ, il y a les disks et les towers.'''
disk_list = [i+1 for i in range(disks)]
# print(f"disk_list : {disk_list}")
# print(type(disk_list))
tower_list = [f"tour_{i+1}"  for i in range(towers)]
# print(f"tower_list : {tower_list}")
# print(type(tower_list))


'''tous les disks sont sur la tour de gauche'''
# towers[0]=disks
# towers[1]=[]
# towers[2]=[]