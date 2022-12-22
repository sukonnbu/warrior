import pygame
import player as pl
import object
import coil
import health_bar
import charge_bar
#import long_button
import sqlite3
import os
from properties import *
from bg import Background
from add_screens import *


#playing = False


pygame.init()


db_path = os.getenv('APPDATA') + "/.warrior4/warrior4.db"


try: conn = sqlite3.connect(db_path)
except:
    os.makedirs(os.getenv('APPDATA') + "/.warrior4")
    conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS score (Score INTEGER);")


class Text():
    def __init__(self):
        self.color = (0, 0, 0)
        self.text = ""
        self.rect = ""

    def draw_text(self, text, rect):
        self.text = def_font.render(text, True, self.color)
        self.rect = rect
        screen.blit(self.text, self.rect)

    def text_color(self, color):
        self.color = color


def main():

    # print(Prop.velocity)

    pygame.init()

    pygame.display.set_caption("Warrior4")
    pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    Prop.set_playing(True)

    title_sound.play(-1)

    #warning_volume = 1

    show_title()

    if not Prop.playing:
        return
    # show_level()

    show_level()

    if not Prop.playing:
        return

    BG1 = Background()
    BG2 = Background()
    BG2.rect = (WIDTH, 0)

    score = 0
    clock = pygame.time.Clock()

    player = pl.Player()
    player.init()

    score_text = Text()
    score_text.text_color((0, 0, 255))

    hp_bar = health_bar.HPBar()
    cg_bar = charge_bar.ChargeBar()

    object1 = object.Object()
    object1.init(0, 500)
    object1.set_speed()

    object2 = object.Object()
    object2.init(1500, 2000)
    object2.set_speed()

    spark = coil.Coil()

    pygame.mixer.music.load("assets/sounds/bg.mp3")
    pygame.mixer.music.play(-1)

    title_sound.stop()

    warning_sound.play(-1)
    warning_sound.set_volume(0)

    while Prop.playing:
        keys = pygame.key.get_pressed()

        is_click = pygame.mouse.get_pressed()

        if keys[pygame.K_UP] or is_click:
            if player.JUMP == 2:
                player.jump(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                Prop.set_playing(False)
                Prop.set_replay(False)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player.JUMP == 0:
                        player.jump(1)
                    elif player.JUMP == 1:
                        player.jump(2)

                if event.key == pygame.K_SPACE:
                    spark.fire_coil()

                if event.key == pygame.K_ESCAPE:
                    show_settings()

                    if not Prop.playing:
                        Prop.set_replay(False)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.JUMP == 0:
                        player.jump(1)
                    elif player.JUMP == 1:
                        player.jump(2)
                if event.button == 3:
                    spark.fire_coil()

        is_spark_collide1 = pygame.Rect.colliderect(object1.rect, spark.rect)
        is_spark_collide2 = pygame.Rect.colliderect(object2.rect, spark.rect)

        if spark.is_visible:
            if is_spark_collide1:
                if object1.hit_coil():
                    Prop.set_playing(False)

            if is_spark_collide2:
                if object2.hit_coil():
                    Prop.set_playing(False)

        is_collide1 = pygame.Rect.colliderect(player.rect, object1.rect)
        is_collide2 = pygame.Rect.colliderect(player.rect, object2.rect)

        if is_collide1:
            hit_sound.play()
            player.collide(object1.type)
            object1.collide()

        if is_collide2:
            hit_sound.play()
            player.collide(object2.type)
            object2.collide()

        if not is_collide1 and not is_collide2:
            player.set_collide_state(False)

        if player.hp <= 1000:
            hp_bar.color = (240, 0, 0)

            if Prop.warning:
                warning_sound.set_volume(0.5)
            else:
                warning_sound.set_volume(0)

            if player.hp <= 0:
                Prop.set_playing(False)

        player.update()
        object1.update(clock.get_time())
        object2.update(clock.get_time())

        spark.update(player.rect.centery)

        score += 10

        BG1.fill_bg()
        BG2.fill_bg()

        player.draw_player()
        object1.draw_object()
        object2.draw_object()
        spark.draw_coil()

        hp_bar.update(player.hp)
        cg_bar.update(spark.charge)
        score_text.draw_text("score: %d" % score, (670, 30))

        clock.tick(60)
        pygame.display.flip()

    pygame.mixer.music.stop()
    warning_sound.stop()

    c.execute("INSERT INTO score VALUES (%d);" % (score))
    conn.commit()

    if Prop.replay:
        show_score(score, c)

        if Prop.playing:
            main()

    conn.close()
    pygame.quit()


if __name__ == '__main__':
    main()
