import pygame
pygame.init()


class Prop():
    def __init__(self):
        self.playing = False
        self.replay = True
        self.velocity = 0
        self.obs_speed = 0
        self.warning = False

    def set_playing(self, playing: bool):
        self.playing = playing

    def set_velocity(self, vel: int):
        self.velocity = vel

    def set_obs_speed(self, speed: int):
        self.obs_speed = speed

    def set_warning(self, warning: bool):
        self.warning = warning

    def set_replay(self, replay: bool):
        self.replay = replay


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


Prop = Prop()
