import pygame

class Graphic():
    def __init__(self):

        # Color
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
        
        
        # Font
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
        
    # Rectangle    
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),0, radius)
        return button
    
    def rect_full_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button
    
    def element(self):
        self.screen_color(self.white)
        self.text_not_align(self.font,50,"Tower Hanoi",self.black,250,50)
        # Down
        self.rect_full_border(self.brown,100,400,160,10,0,5)
        self.rect_full_border(self.brown,400,400,160,10,0,5)
        self.rect_full_border(self.brown,700,400,160,10,0,5)
        
        # Up
        self.rect_full_border(self.brown,100,325,10,150,0,5)
        self.rect_full_border(self.brown,400,325,10,150,0,5)
        self.rect_full_border(self.brown,700,325,10,150,0,5)
        
        # Palette
        self.rect_full_border(self.pal1,100,387,150,15,0,5)
        self.rect_full_border(self.pal2,100,372,140,15,0,5)
        self.rect_full_border(self.pal3,100,357,130,15,0,5)
        self.rect_full_border(self.pal4,100,342,120,15,0,5)
        self.rect_full_border(self.pal5,100,327,110,15,0,5)
        self.rect_full_border(self.pal6,100,312,100,15,0,5)
        self.rect_full_border(self.pal7,100,297,90,15,0,5)
        self.rect_full_border(self.pal8,100,282,80,15,0,5)
        
        # self.rect_full_border(self.pal1,400,387,150,15,0,5)
        # self.rect_full_border(self.pal2,400,372,140,15,0,5)
        # self.rect_full_border(self.pal3,400,357,130,15,0,5)
        # self.rect_full_border(self.pal4,400,342,120,15,0,5)
        # self.rect_full_border(self.pal5,400,327,110,15,0,5)
        # self.rect_full_border(self.pal6,400,312,100,15,0,5)
        # self.rect_full_border(self.pal7,400,297,90,15,0,5)
        # self.rect_full_border(self.pal8,400,282,80,15,0,5)

        # self.rect_full_border(self.pal1,700,387,150,15,0,5)
        # self.rect_full_border(self.pal2,700,372,140,15,0,5)
        # self.rect_full_border(self.pal3,700,357,130,15,0,5)
        # self.rect_full_border(self.pal4,700,342,120,15,0,5)
        # self.rect_full_border(self.pal5,700,327,110,15,0,5)
        # self.rect_full_border(self.pal6,700,312,100,15,0,5)
        # self.rect_full_border(self.pal7,700,297,90,15,0,5)
        # self.rect_full_border(self.pal8,700,282,80,15,0,5)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            self.element()
            self.update()
game_page = Graphic()
game_page.run()