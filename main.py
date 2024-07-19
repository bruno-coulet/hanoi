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

# Pour récupérer les paramètres depuis l'appel du fichier: python main.py (argument1, argument2)
# Le premier argument (index 0) estant le nom du fichier.

# import sys
# argument1 = sys.argv[1]
# argument2 = sys.argv[2]

game_page = MainRun()
game_page.running()
