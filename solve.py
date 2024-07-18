from main import disks, towers, disk_list, tower_list

moves = []

print(f"disques : {disks}")
print(f"tours : {towers}")

def solve(tower_1, tower_3, tower_2, disks):
    if disks > 0:
        solve(tower_1, tower_2, tower_3, disks - 1)
        moves.append((tower_1, tower_3))
        solve(tower_2, tower_3, tower_1, disks - 1)
    return tower_1, tower_3, tower_2


# Appel de la fonction solve pour résoudre le problème de la Tour de Hanoï
solve(tower_list[0], tower_list[2], tower_list[1], disks)

print(f"moves : {moves}")