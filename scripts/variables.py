import pygame

pygame.init()


screen_size = WIDTH, HEIGHT = 1000, 600
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode(screen_size)

title_font = pygame.font.SysFont('freesanbold', 150, True)
def_font = pygame.font.SysFont('freesanbold.ttf', 75)

click_sound = pygame.mixer.Sound("assets/sounds/click.mp3")
hit_sound = pygame.mixer.Sound("assets/sounds/hit.mp3")

title_sound = pygame.mixer.Sound("assets/sounds/waiting.wav")
laser_sound = pygame.mixer.Sound("assets/sounds/Laser.wav")
warning_sound = pygame.mixer.Sound("assets/sounds/warn.wav")
gameover_sound = pygame.mixer.Sound("assets/sounds/game_end.wav")

click_sound.set_volume(1)
hit_sound.set_volume(1)
title_sound.set_volume(0.5)
laser_sound.set_volume(1)
gameover_sound.set_volume(0.5)
warning_sound.set_volume(0.5)
pygame.mixer.music.set_volume(1)
