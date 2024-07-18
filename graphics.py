import pygame


# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
brown = "#7c5f3f"
pal1 = "#FF5EFA"
pal2 = "#FF7AD1"
pal3 = "#FF96A5"
pal4 = "#FFB875"
pal5 = "#FFD754"
pal6 = "#F99F72"
pal7 = "#FE895E"
pal8 = "#DA7B27"
solving = False

# Police d'écriture
font = "Comic Pillow.otf"

# Initialiser l'écran
pygame.init()
W = 800
H = 600
Window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tours de Hanoi")
clock = pygame.time.Clock()

# État des tours
t_1 = list(range(8, 0, -1))  # Les disques de 8 à 1 sur la Tour_1
t_2 = []
t_3 = []

# Index de mouvement actuel
move_index = 0
moves = []

# Méthode de mise à jour de l'écran
def update(self):
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    Window.fill((0, 0, 0))

def screen_color(self, color): 
    Window.fill(color)

# Méthode pour centrer le texte
def text_center(self, font, text_size, text_content, color, x, y):
    pygame.font.init()
    text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
    text_rect = text.get_rect(center=(x, y))
    Window.blit(text, text_rect)

# Méthode pour dessiner un rectangle plein
def rect_full(self, color, x, y, width, height, radius):
    button = pygame.draw.rect(Window, color, pygame.Rect(x, y, width, height), 0, radius)
    return button

# Méthode pour dessiner un rectangle avec bordure pleine
def rect_full_border(self, color, x, y, width, height, thickness, radius):
    button = pygame.draw.rect(Window, color, pygame.Rect(x - width // 2, y - height // 2, width, height), thickness, radius)
    return button

# Méthode pour dessiner un rectangle avec bordure
def rect_border(self, color, x, y, width, height, thickness, radius):
    button = pygame.draw.rect(Window, color, pygame.Rect(x - width // 2, y - height // 2, width, height), thickness, radius)
    return button

# Méthode pour vérifier si la souris est au-dessus d'un bouton
def is_mouse_over_button(self, button_rect):
    mouse_pos = pygame.mouse.get_pos()
    return button_rect.collidepoint(mouse_pos)

# Méthode pour gérer l'animation du survol d'un bouton
def button_hover(name, x, y, width, height, color_full, color_border, color_border_hover, text, font, text_color, text_size, thickness, radius): 
    name = pygame.Rect((x - width // 2), (y - height // 2), width, height)
    if is_mouse_over_button(name):
        rect_border(color_border_hover, x, y, width + 5, height + 5, thickness, radius)
    else:
        rect_full(color_full, x, y, width, height, radius)
        rect_border(color_border, x, y, width, height, thickness, radius)
    text_center(font, text_size, text, text_color, x, y)
    return name 

# Méthode pour dessiner les éléments de l'écran
def element():
    screen_color(white)
    text_center(font, 50, "Tower Hanoi", black, 400, 50)
    button_solve = button_hover("resolution", 400, 500, 150, 100, white, pal4, pal4, "Solver", font, black, 25, 0, 5)

# Dessiner les tours
rect_full_border(brown, 100, 400, 160, 10, 0, 5)
rect_full_border(brown, 400, 400, 160, 10, 0, 5)
rect_full_border(brown, 700, 400, 160, 10, 0, 5)
rect_full_border(brown, 100, 325, 10, 150, 0, 5)
rect_full_border(brown, 400, 325, 10, 150, 0, 5)
rect_full_border(brown, 700, 325, 10, 150, 0, 5)

# Dessiner les disques sur les tours
draw_disks()

# Méthode pour dessiner les disques sur les tours
def draw_disks(self):
colors = [pal1, pal2, pal3, pal4, pal5, pal6, pal7, pal8]

# Dessiner les disques sur la Tour 1
for i, disk in enumerate(t_1):
    rect_full_border(colors[disk-1], 100, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)

# Dessiner les disques sur la Tour 2
for i, disk in enumerate(t_2):
    rect_full_border(colors[disk-1], 400, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)

# Dessiner les disques sur la Tour 3
for i, disk in enumerate(t_3):
    rect_full_border(colors[disk-1], 700, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)

# Méthode pour exécuter un mouvement
def execute_move(self):
    if move_index < len(moves):
        from_tower, to_tower = moves[move_index]
        print(moves[move_index])
        if from_tower == "1":
            disk = t_1.pop()
            print("ok1")
        elif from_tower == "2":
            disk = t_2.pop()
            print("ok2")
        else:
            disk = t_3.pop()
            print("ok3")

        if to_tower == "1":
            t_1.append(disk)
            print("ok1_1")
        elif to_tower == "2":
            t_2.append(disk)
            print("ok2_2")
        else:
            t_3.append(disk)
            print("ok3_3")
            
        move_index += 1
        print(move_index)

    # Méthode principale pour exécuter le jeu
def run(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_solve.collidepoint(event.pos):
                    solving = True
        if solving:
            execute_move()
            pygame.time.wait(10)
        element()
        update()
