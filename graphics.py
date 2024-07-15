import pygame

class Graphic():
    def __init__(self):

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.font = "Comic Pillow.otf"
        
    # Writte text methode
    def text_not_align(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)