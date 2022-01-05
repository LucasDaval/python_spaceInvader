import pygame
class joueur:
    def __init__(self):
        self.X = 10
        self.Y = 250
    
    def update(self, event):
        if event.key == pygame.K_z:
            self.Y = self.Y - 20
        if event.key == pygame.K_s:
            self.Y = self.Y + 20

    def draw(self, ecran):
        pygame.draw.circle(ecran, (112, 123, 124), (self.X, self.Y), 20)