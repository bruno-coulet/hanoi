class Solver:
    def solve(self, t_1, t_3, t_2, disks, moves):
        if disks > 0:
            self.solve(t_1, t_2, t_3, disks - 1, moves)
            moves.append((t_1, t_3))
            self.solve(t_2, t_3, t_1, disks - 1, moves)

    def solve_terminal(self, t_1, t_3, t_2, disks):
        if disks > 0:
            self.solve_terminal(t_1, t_2, t_3, disks - 1)
            print(t_1, "->", t_3)
            self.solve_terminal(t_2, t_3, t_1, disks - 1)

# solver_terminal = Solver()
# solver_terminal.solve_terminal("1", "3", "2", 16)
