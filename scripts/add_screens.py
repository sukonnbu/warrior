from properties import *
import long_button
import square_button
import math


is_muted = False


def show_title():
    #global playing

    Title = title_font.render("WARRIOR4", True, (150, 150, 150))
    Title2 = title_font.render("WARRIOR4", True, (50, 50, 50))

    title_image = pygame.image.load("assets/images/title.png")
    title_rect = title_image.get_rect()
    title_rect.center = (WIDTH / 2, HEIGHT / 2 - 50)

    start_button = long_button.Button()
    start_button.init_button("assets/images/start_button_on.png",
                             "assets/images/start_button_off.png", (850, HEIGHT - 120))

    turn_page = False
    mouse_on = False

    #playing = True

    while not turn_page:

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if start_button.rect.x + 200 > mouse_pos[0] > start_button.rect.x and start_button.rect.y + 70 > mouse_pos[1] > start_button.rect.y:
            mouse_on = True

            if is_click[0]:
                click_sound.play()
                pygame.time.wait(100)
                turn_page = True
        else:
            mouse_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                Prop.set_playing(False)
                turn_page = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mouse_on = True
                    start_button.update(mouse_on)
                    start_button.draw()
                    click_sound.play()

                    pygame.time.wait(100)
                    turn_page = True

                elif event.key == pygame.K_ESCAPE:

                    show_settings()

                    if not Prop.get_playing():
                        turn_page = True

        start_button.update(mouse_on)

        screen.fill(BG_COLOR)

        screen.blit(Title2, (65, HEIGHT - 165))
        screen.blit(Title, (60, HEIGHT - 165))

        screen.blit(title_image, title_rect)

        start_button.draw()

        pygame.display.flip()


def show_level():
    # velocity, obs_speed = 0, 0  # , playing

    easy = long_button.Button()
    normal = long_button.Button()
    hard = long_button.Button()

    easy.init_button("assets/images/easy_on.png",
                     "assets/images/easy_off.png", (250, 400))
    normal.init_button("assets/images/norm_on.png",
                       "assets/images/norm_off.png", (500, 400))
    hard.init_button("assets/images/hard_on.png",
                     "assets/images/hard_off.png", (750, 400))

    turn_page = False

    Buttons = [easy, normal, hard]
    Mouse_ons = [False, False, False]  # easy, norm, hard

    while not turn_page:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                Prop.set_playing(False)
                turn_page = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    show_settings()

                    if not Prop.get_playing():
                        turn_page = True

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        # Working
        for i in range(len(Buttons)):
            if Buttons[i].rect.x + 200 > mouse_pos[0] > Buttons[i].rect.x and Buttons[i].rect.y + 70 > mouse_pos[1] > Buttons[i].rect.y:
                Mouse_ons[i] = True

                if is_click[0]:
                    click_sound.play()

                    Prop.set_difficulty(i)

                    turn_page = True
            else:
                Mouse_ons[i] = False

            Buttons[i].update(Mouse_ons[i])
            Buttons[i].draw()

        pygame.display.flip()


def show_score(score, c):
    #global playing

    scores = c.execute("SELECT SCORE FROM score;")
    max_score = 0

    for i in scores:
        if i[0] > max_score:
            max_score = i[0]

    score_text = def_font.render("score: %d" % score, True, (0, 240, 0))
    score_rect = score_text.get_rect()
    score_rect.center = (WIDTH / 2, HEIGHT / 2 + 80)

    max_score_text = def_font.render(
        "max score: %d" % max_score, True, (0, 0, 240))
    max_score_rect = max_score_text.get_rect()
    max_score_rect.center = (WIDTH / 2, HEIGHT / 2 + 140)

    gameover_text = title_font.render("Game Over", True, (240, 0, 0))
    gameover_rect = gameover_text.get_rect()
    gameover_rect.center = (WIDTH / 2, HEIGHT / 2 - 100)

    screen.fill(BG_COLOR)

    screen.blit(gameover_text, gameover_rect)
    screen.blit(score_text, score_rect)
    screen.blit(max_score_text, max_score_rect)

    start_button = long_button.Button()
    start_button.init_button("assets/images/restart_button_on.png",
                             "assets/images/restart_button_off.png", (850, HEIGHT - 120))  # replay

    turn_page = False
    mouse_on = False

    #playing = True

    gameover_sound.play()

    while not turn_page:

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if start_button.rect.x + 200 > mouse_pos[0] > start_button.rect.x and start_button.rect.y + 70 > mouse_pos[1] > start_button.rect.y:
            mouse_on = True

            if is_click[0]:
                click_sound.play()
                pygame.time.wait(100)
                Prop.set_playing(True)
                turn_page = True
        else:
            mouse_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                Prop.set_playing(False)
                turn_page = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mouse_on = True
                    start_button.update(mouse_on)
                    start_button.draw()
                    click_sound.play()

                    pygame.time.wait(100)
                    Prop.set_playing(True)
                    turn_page = True

                # elif event.key == pygame.K_ESCAPE:

                #    turn_page = True
                #    playing = False

        start_button.update(mouse_on)

        start_button.draw()

        pygame.display.flip()

    gameover_sound.stop()


def show_settings():

    global is_muted

    mute_button = square_button.Button()
    mute_button.init_button("assets/images/muted.png",
                            "assets/images/not_muted.png", (850, HEIGHT - 120))

    #playing = True
    turn_page = False

    while not turn_page:

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if mute_button.rect.x + 70 > mouse_pos[0] > mute_button.rect.x and mute_button.rect.y + 70 > mouse_pos[1] > mute_button.rect.y:

            if is_click[0]:
                click_sound.play()
                pygame.time.wait(100)

                if is_muted:
                    is_muted = False
                    click_sound.set_volume(1)
                    hit_sound.set_volume(1)
                    title_sound.set_volume(1)
                    laser_sound.set_volume(1)
                    gameover_sound.set_volume(1)
                    pygame.mixer.music.set_volume(1)
                    Prop.set_warning(True)

                else:
                    is_muted = True
                    click_sound.set_volume(0)
                    hit_sound.set_volume(0)
                    title_sound.set_volume(0)
                    laser_sound.set_volume(0)
                    gameover_sound.set_volume(0)
                    pygame.mixer.music.set_volume(0)
                    Prop.set_warning(False)
                    warning_sound.set_volume(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                Prop.set_playing(False)
                turn_page = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    turn_page = True
                    # Prop.set_playing(True)

        mute_button.update(is_muted)

        screen.fill(BG_COLOR)
        mute_button.draw()

        pygame.display.flip()
