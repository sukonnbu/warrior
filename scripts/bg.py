import pygame
from properties import *


class Background():
    def __init__(self):
        self.image = pygame.image.load("assets/images/BG.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect = (0, 0)
        self.speed = 5  # 1/n pixels per ms
        self.current = 0

    def fill_bg(self):
        self.current += 1

        if self.rect[0] <= -WIDTH:
            self.rect = (WIDTH, 0)

        if self.current / self.speed == 1:
            self.rect = (self.rect[0] - 1, self.rect[1])
            self.current = 0

        screen.blit(self.image, self.rect)
