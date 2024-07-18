from main import total_disks, total_towers

moves = []
disks = total_disks


def solve(t_1, t_3, t_2, disks):
    if disks > 0:
        solve(t_1, t_2, t_3, disks - 1)
        moves.append((t_1, t_3))
        solve(t_2, t_3, t_1, disks - 1)
    return t_1, t_3, t_2

print(moves)