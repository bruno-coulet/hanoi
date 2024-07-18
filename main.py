from solve import solve
from graphics import *


disks=int(input("Choisissez un nombre de disque :"))
towers=int(input("Choisissez un nombre de tour :"))
start_string=f"{towers},{disks}"
print(start_string)

disk_list = [i+1 for i in range(disks)]
# print(f"disk_list : {disk_list}")
# print(type(disk_list))
tower_list = [f"tour_{i+1}"  for i in range(towers)]

class MainRun():
    def __init__(self):
        solve(self)
        graphic(self)
        self.moves = []
        self.move_index = 0

    def running(self):
        self.solve("1", "3", "2", disks, self.moves)
        self.run()
        
game_page = MainRun()
game_page.running()