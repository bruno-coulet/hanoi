import pygame
import sys
from main import disks, tower_list
from solve import solve

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TOWER_WIDTH = 20
TOWER_HEIGHT = SCREEN_HEIGHT*0.6
# TOWER_HEIGHT = 100
DISK_HEIGHT = 20
DISK_COLOR = (0, 128, 255)
TOWER_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (100, 100, 100)
MOVE_DELAY = 500  # milliseconds par mouvement

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
clock = pygame.time.Clock()

# Calculate tower positions
tower_positions = [
    (SCREEN_WIDTH // 4, TOWER_HEIGHT+50),
    (SCREEN_WIDTH // 2, SCREEN_HEIGHT - TOWER_HEIGHT // 2),
    (3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - TOWER_HEIGHT // 2)
]

# Function to draw towers
def draw_towers():
    for x, y in tower_positions:
        pygame.draw.rect(screen, TOWER_COLOR, (x - TOWER_WIDTH // 2, y - 300, TOWER_WIDTH, 400))

# Function to draw disks
def draw_disks(tower_state):
    for i, tower in enumerate(tower_state):
        x, y = tower_positions[i]
        for j, disk in enumerate(tower):
            disk_width = disk * 20
            pygame.draw.rect(screen, DISK_COLOR, (x - disk_width // 2, y - (j + 1) * DISK_HEIGHT, disk_width, DISK_HEIGHT))

# Solve and initialize state
tower_state = [list(reversed(range(1, disks + 1))), [], []]
moves = []
solve(tower_list[0], tower_list[2], tower_list[1], disks)

# Flatten the moves list to get a sequential animation of disk movements
animated_moves = [(tower_list.index(from_tower), tower_list.index(to_tower)) for from_tower, to_tower in moves]

# Main loop function
def main():
    move_index = 0
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_towers()
        draw_disks(tower_state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Execute moves
        if move_index < len(animated_moves):
            from_tower_index, to_tower_index = animated_moves[move_index]
            from_tower, to_tower = tower_positions[from_tower_index], tower_positions[to_tower_index]
            disk = tower_state[from_tower_index].pop()
            tower_state[to_tower_index].append(disk)
            move_index += 1

            # Delay for visualization
            pygame.time.wait(MOVE_DELAY)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()




# import pygame
# import sys
# from main import disks, tower_list
# from solve import solve

# # Constants
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# TOWER_WIDTH = 20
# DISK_HEIGHT = 20
# DISK_COLOR = (0, 128, 255)
# TOWER_COLOR = (0, 0, 0)
# BACKGROUND_COLOR = (255, 255, 255)

# # Pygame setup
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Tower of Hanoi")
# clock = pygame.time.Clock()

# # Calculate tower positions
# tower_positions = [
#     (SCREEN_WIDTH // 4, SCREEN_HEIGHT - 100),
#     (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100),
#     (3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - 100)
# ]

# # Draw tower function
# def draw_towers():
#     for x, y in tower_positions:
#         pygame.draw.rect(screen, TOWER_COLOR, (x - TOWER_WIDTH // 2, y - 300, TOWER_WIDTH, 400))

# # Draw disks function
# def draw_disks(tower_state):
#     for i, tower in enumerate(tower_state):
#         x, y = tower_positions[i]
#         for j, disk in enumerate(tower):
#             disk_width = disk * 20
#             pygame.draw.rect(screen, DISK_COLOR, (x - disk_width // 2, y - (j + 1) * DISK_HEIGHT, disk_width, DISK_HEIGHT))

# # Solve and initialize state
# tower_state = [list(reversed(range(1, disks + 1))), [], []]
# moves = []
# solve(tower_list[0], tower_list[2], tower_list[1], disks)

# def main():
#     global moves
#     move_index = 0
#     move_delay = 500  # milliseconds per move

#     while True:
#         screen.fill(BACKGROUND_COLOR)
#         draw_towers()
#         draw_disks(tower_state)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Execute moves
#         if move_index < len(moves):
#             pygame.time.wait(move_delay)
#             from_tower, to_tower = moves[move_index]
#             disk = tower_state[tower_list.index(from_tower)].pop()
#             tower_state[tower_list.index(to_tower)].append(disk)
#             move_index += 1

#         pygame.display.flip()
#         clock.tick(60)

# if __name__ == "__main__":
#     main()
