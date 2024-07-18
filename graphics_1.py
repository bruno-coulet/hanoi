import pygame
from solve_2 import solver

class Graphic(solver):
    def __init__(self):
        # Initialiser la classe de résolution (solver)
        solver.__init__(self)

        # Couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.brown = "#7c5f3f"
        self.pal1 = "#FF5EFA"
        self.pal2 = "#FF7AD1"
        self.pal3 = "#FF96A5"
        self.pal4 = "#FFB875"
        self.pal5 = "#FFD754"
        self.pal6 = "#F99F72"
        self.pal7 = "#FE895E"
        self.pal8 = "#DA7B27"
        self.solving = False

        # Police d'écriture
        self.font = "Comic Pillow.otf"
        
        # Initialiser l'écran
        pygame.init()
        self.W = 800
        self.H = 600
        self.Window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Hanoi")
        self.clock = pygame.time.Clock()
        
        # État des tours
        self.t_1 = list(range(8, 0, -1))  # Les disques de 8 à 1 sur la Tour_1
        self.t_2 = []
        self.t_3 = []
        self.moves = []

        # Index de mouvement actuel
        self.move_index = 0
        
    # Méthode de mise à jour de l'écran
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Window.fill((0, 0, 0))

    def screen_color(self, color): 
        self.Window.fill(color)
        
    # Méthode pour centrer le texte
    def text_center(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)
        
    # Méthode pour dessiner un rectangle plein
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height), 0, radius)
        return button
    
    # Méthode pour dessiner un rectangle avec bordure pleine
    def rect_full_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width // 2, y - height // 2, width, height), thickness, radius)
        return button

    # Méthode pour dessiner un rectangle avec bordure
    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width // 2, y - height // 2, width, height), thickness, radius)
        return button
    
    # Méthode pour vérifier si la souris est au-dessus d'un bouton
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
    
    # Méthode pour gérer l'animation du survol d'un bouton
    def button_hover(self, name, x, y, width, height, color_full, color_border, color_border_hover, text, font, text_color, text_size, thickness, radius): 
        name = pygame.Rect((x - width // 2), (y - height // 2), width, height)
        if self.is_mouse_over_button(name):
            self.rect_border(color_border_hover, x, y, width + 5, height + 5, thickness, radius)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
        self.text_center(font, text_size, text, text_color, x, y)
        return name 

    # Méthode pour dessiner les éléments de l'écran
    def element(self):
        self.screen_color(self.white)
        self.text_center(self.font, 50, "Tower Hanoi", self.black, 400, 50)
        self.button_solve = self.button_hover("resolution", 400, 500, 150, 100, self.white, self.pal4, self.pal4, "Solver", self.font, self.black, 25, 0, 5)
        
        # Dessiner les tours
        self.rect_full_border(self.brown, 100, 400, 160, 10, 0, 5)
        self.rect_full_border(self.brown, 400, 400, 160, 10, 0, 5)
        self.rect_full_border(self.brown, 700, 400, 160, 10, 0, 5)
        self.rect_full_border(self.brown, 100, 325, 10, 150, 0, 5)
        self.rect_full_border(self.brown, 400, 325, 10, 150, 0, 5)
        self.rect_full_border(self.brown, 700, 325, 10, 150, 0, 5)
        
        # Dessiner les disques sur les tours
        self.draw_disks()

    # Méthode pour dessiner les disques sur les tours
    def draw_disks(self):
        colors = [self.pal1, self.pal2, self.pal3, self.pal4, self.pal5, self.pal6, self.pal7, self.pal8]
            
        # Dessiner les disques sur la Tour 1
        for i, disk in enumerate(self.t_1):
            self.rect_full_border(colors[disk-1], 100, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)
        
        # Dessiner les disques sur la Tour 2
        for i, disk in enumerate(self.t_2):
            self.rect_full_border(colors[disk-1], 400, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)
        
        # Dessiner les disques sur la Tour 3
        for i, disk in enumerate(self.t_3):
            self.rect_full_border(colors[disk-1], 700, 387 - i * 15, 150 - (8 - disk) * 10, 15, 0, 5)
    
    # Méthode pour exécuter un mouvement
    def execute_move(self):
        if self.move_index < len(self.moves):
            from_tower, to_tower = self.moves[self.move_index]
            if from_tower == "Tour_1":
                disk = self.t_1.pop()
                self.solving = False
            elif from_tower == "Tour_2":
                disk = self.t_2.pop()
                self.solving = False
            else:
                disk = self.t_3.pop()
                self.solving = False

            if to_tower == "Tour_1":
                self.t_1.append(disk)
                self.solving = False
            elif to_tower == "Tour_2":
                self.t_2.append(disk)
                self.solving = False
            else:
                self.t_3.append(disk)
                self.solving = False
                
            self.move_index += 1

    # Méthode principale pour exécuter le jeu
    def run(self):
        self.solve("Tour_1", "Tour_3", "Tour_2", 8)
        solving = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_solve.collidepoint(event.pos):
                        self.solving = True
            if self.solving:
                self.execute_move()
                # pygame.time.wait(500)  # Attendre un peu avant le prochain mouvement (facultatif)
            self.element()
            self.update()

# Initialiser et exécuter le jeu
game_page = Graphic()
game_page.run()
