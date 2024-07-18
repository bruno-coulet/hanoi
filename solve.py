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





# class Solver():
#     def solve(self, t_1, t_3, t_2, disks, moves):
#         if disks > 0:
#             self.solve(t_1, t_2, t_3, disks - 1, moves)
#             moves.append((t_1, t_3))
#             self.solve(t_2, t_3, t_1, disks - 1, moves)
