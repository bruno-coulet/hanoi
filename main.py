from solve import Solver
from graphics import Graphic

class MainRun(Solver, Graphic):
    def __init__(self):
        Solver.__init__(self)
        Graphic.__init__(self)
        self.moves = []
        self.move_index = 0

    def running(self):
        self.solve("1", "3", "2", 8, self.moves)
        self.run()
        
game_page = MainRun()
game_page.running()