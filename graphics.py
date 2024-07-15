import pygame

class Graphic():
    def __init__(self):

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.font = "Comic Pillow.otf"
        # Screen 
        pygame.init()
        self.W = 800
        self.H = 600
        self.Window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Hanoi")
        self.clock = pygame.time.Clock()
        
    # Screen methode
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(155)
        self.Window.fill((0, 0, 0))

    def screen_color(self, color): 
        self.Window.fill(color)
        
    # Writte text methode
    def text_not_align(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            self.screen_color(self.white)
            self.update()
game_page = Graphic()
game_page.run()