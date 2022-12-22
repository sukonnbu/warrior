import pygame
from properties import *


class Background():
    def __init__(self):
        self.image = pygame.image.load("assets/images/BG.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect = (0, 0)

    def fill_bg(self):

        if self.rect[0] <= -WIDTH:
            self.rect = (WIDTH, 0)

        self.rect = (self.rect[0] - 1, self.rect[1])
        screen.blit(self.image, self.rect)
