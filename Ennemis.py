import pygame
import math
from random import randrange

class ennemis:
    def __init__(self, status, target, range):
        self.X = 500
        self.Y = randrange(target - range, target + range)
        self.size = randrange(10, 30)
        self.Cond = status


    def draw(self, ecran):
        pygame.draw.circle(ecran, (102, 38, 24), (self.X, self.Y), self.size)

    def update(self, time, spd):
        if self.Cond == 1:
            self.Y += math.sin(time/1000)
            self.X -= 1.3
        else:
            self.X -= spd
        
