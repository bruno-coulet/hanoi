# solve.py

moves = []

def solve(t_1, t_3, t_2, disks):
    if disks > 0:
        solve(t_1, t_2, t_3, disks - 1)
        moves.append((t_1, t_3))
        solve(t_2, t_3, t_1, disks - 1)

solve("Tour_1", "Tour_3", "Tour_2", 8)

# Initialisation des tours avec les disques

# Tour 1
t_1 = list(range(8, 0, -1))  # Les disques de 8 à 1 sur la Tour_1

# Tour 2
t_2 = []

# Tour 3
t_3 = []

# Effectuer les mouvements en mettant à jour les tours
def lists():
    for move in moves:
        from_tower, to_tower = move
        if from_tower == "Tour_1":
            disk = t_1.pop()
        elif from_tower == "Tour_2":
            disk = t_2.pop()
        else:
            disk = t_3.pop()
        
        if to_tower == "Tour_1":
            t_1.append(disk)
        elif to_tower == "Tour_2":
            t_2.append(disk)
        else:
            t_3.append(disk)

# Afficher les tours après tous les mouvements
lists()
print("Final state of Tour_1:", t_1)
print("Final state of Tour_2:", t_2)
print("Final state of Tour_3:", t_3)
