from solve import Solver
from graphics import Graphic


class MainRun(Solver, Graphic):
    def __init__(self):
        Solver.__init__(self)
        Graphic.__init__(self)
        self.moves = []
        self.move_index = 0
        self.t_1 = list(range(8, 0, -1))
        self.t_2 = []
        self.t_3 = []

    def running(self):
        self.solve("1", "3", "2", 8, self.moves)
        self.run()


game_page = MainRun()
game_page.running()
