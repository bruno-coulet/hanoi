import pygame

class Graphic():
    def __init__(self):
        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.brown = "#7c5f3f"
        self.palette_colors = ["#FF5EFA", "#FF7AD1", "#FF96A5", "#FFB875", "#FFD754", "#F99F72", "#FE895E", "#DA7B27"]
        
        # Font
        self.font = "Comic Pillow.otf"
        
        # Screen 
        pygame.init()
        self.W = 800
        self.H = 600
        self.Window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Hanoi")
        self.clock = pygame.time.Clock()
        
        # Palette positions
        self.palettes = [(100, 387 - i * 15, 150 - i * 10, 15) for i in range(8)]
        self.selected_palette = None
        self.pegs = [(100, 325), (400, 325), (700, 325)]
        self.piles = [[i for i in range(8)], [], []]  # Initial state with all palettes on the first peg
        
    # Screen methods
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(155)
        self.Window.fill((0, 0, 0))

    def screen_color(self, color): 
        self.Window.fill(color)
        
    # Write text method
    def text_not_align(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)
        
    # Rectangle methods
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height), 0, radius)
        return button
    
    def rect_full_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width // 2, y - height // 2, width, height), thickness, radius)
        return button
    
    def draw_element(self):
        self.screen_color(self.white)
        self.text_not_align(self.font, 50, "Tower Hanoi", self.black, 250, 50)
        
        # Down
        for x in [100, 400, 700]:
            self.rect_full_border(self.brown, x, 400, 160, 10, 0, 5)

        # Up
        self.up_1 = self.rect_full_border(self.brown, 100, 325, 10, 150, 0, 5)
        self.up_2 = self.rect_full_border(self.brown, 400, 325, 10, 150, 0, 5)
        self.up_3 = self.rect_full_border(self.brown, 700, 325, 10, 150, 0, 5)
        
        # Palettes
        for i, (x, y, width, height) in enumerate(self.palettes):
            self.rect_full_border(self.palette_colors[i], x, y, width, height, 0, 5)
    
    def handle_click(self, pos):
        x, y = pos
        for i, (px, py, width, height) in enumerate(self.palettes):
            if px - width // 2 <= x <= px + width // 2 and py - height // 2 <= y <= py + height // 2:
                self.selected_palette = i
                return
        
        for peg_index, (peg_x, peg_y) in enumerate(self.pegs):
            if peg_x - 50 <= x <= peg_x + 50 and peg_y - 75 <= y <= peg_y + 75:
                if self.selected_palette is not None:
                    self.move_palette(self.selected_palette, peg_index)
                    self.selected_palette = None
                return
    
    def move_palette(self, palette_index, peg_index):
        # Find current peg index of the selected palette
        current_peg_index = next(i for i, pile in enumerate(self.piles) if palette_index in pile)
        if current_peg_index == peg_index:
            return  # Do nothing if the palette is moved to the same peg
        
        # Check if the move is valid
        if self.piles[peg_index] and self.piles[peg_index][-1] < palette_index:
            self.text_not_align(self.font,20,"Invalid move: cannot place larger palette on smaller one",self.black,150,80)
            return  # Invalid move: cannot place larger palette on smaller one
        
        # Move the palette
        self.piles[current_peg_index].remove(palette_index)
        self.piles[peg_index].append(palette_index)
        
        # Update palette position
        new_x = self.pegs[peg_index][0]
        new_y = 387 - len(self.piles[peg_index]) * 15  # Adjust y position based on the number of palettes on the peg
        self.palettes[palette_index] = (new_x, new_y, self.palettes[palette_index][2], self.palettes[palette_index][3])
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.draw_element()
            self.update()

game_page = Graphic()
game_page.run()
