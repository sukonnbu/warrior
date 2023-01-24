import pygame
import random
from properties import *


speed = 0


class Object():
    def __init__(self):
        self.image = ""
        self.rect = ""
        self.type = ""

        self.is_visible = True

    def set_speed(self):
        global speed
        speed = Prop.get_obs_speed()

    def init(self, start=500, end=2000):
        setting = random.random()
        bottom = 0  # init

        if setting <= 0.4:
            self.type = "iron"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/images/iron.png"), (150, 75))
            bottom = HEIGHT - 5

        elif setting <= 0.9:
            self.type = "bullet"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/images/bullet.png"), (150, 50))
            bottom = HEIGHT - 70

        elif setting <= 0.95:
            self.type = "tan"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/images/tan.png"), (100, 100))
            bottom = HEIGHT - 50

        elif setting <= 0.98:
            self.type = "anticarbon"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/images/anticarbon.png"), (100, 100))
            bottom = HEIGHT - 50

        else:
            self.type = "nuclear"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/images/nuclear.png"), (150, 75))
            bottom = HEIGHT - 50

        self.rect = self.image.get_rect()

        self.rect.bottom = bottom
        self.rect.x = WIDTH + random.randint(start, end)

    def draw_object(self):
        if self.is_visible:
            screen.blit(self.image, self.rect)
        else:
            self.init()
            self.is_visible = True

    def update(self, time):
        global speed

        self.rect.x -= speed + round(time/500)

        if self.rect.x < 0:
            self.is_visible = False

            return 500  # extra points

        return 0  # no extra points

    def collide(self):
        self.is_visible = False

    def hit_coil(self):
        if self.type == "iron" or self.type == "bullet" or self.type == "anticarbon":
            self.is_visible = False
            # still playing
            return 0

        elif self.type == "nuclear":
            # gameover
            return 1

        return 0
