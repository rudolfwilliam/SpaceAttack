import pygame
import time
from factory import Factory
from figure import Figure

pygame.init()
rocket_up_img = pygame.image.load("rocket_ship_up.png")
rocket_right_img = pygame.image.load("rocket_ship_right.png")
rocket_down_img = pygame.image.load("rocket_ship_down.png")
rocket_left_img = pygame.image.load("rocket_ship_left.png")

enemyA_img = pygame.image.load("monster_A.png")
enemyB_img = pygame.image.load("monster_B.png")
enemyC_img = pygame.image.load("monster_C.png")
comet_img = pygame.image.load("comet.png")

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Attack")
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 30)
red = (244, 66, 66)
green = (66, 255, 66)
orange = (250, 206, 60)
figure_width = 50
figure_height = 50
enemy_width = 30
enemy_height = 30
comet_width = 30
comet_height = 30
x = (display_width / 2) - (figure_width / 2)
y = (display_height / 2) - (figure_height / 2)
spawn_counter = 240
highscore = 0

figure = Figure(x, y, display_width, display_height)
factory = Factory(figure, display_width, display_height)

def crash(highscore, score):
    message_display("Your Spaceship Crashed!", highscore, score)

def message_display(text, highscore, score):
    font = pygame.font.Font('Futura.ttc', 50)
    gameDisplay.blit(font.render(text, True, orange), (140, 280))
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT, 2000)

    should_quit = False

    while not should_quit:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                should_quit = True
    spawn_counter = 240
    figure.x = (display_width / 2) - (figure_width / 2)
    figure.y = (display_height / 2) - (figure_height / 2)
    if (score > highscore):
        highscore = score
    game_loop(spawn_counter, highscore, clock)

def rocket_ship(x, y, x_change, y_change, before):
    if y_change == 0 and x_change == 0:
        gameDisplay.blit(before, (x - 25, y - 23))
        return before
    elif y_change > 0:
        gameDisplay.blit(rocket_down_img, (x - 25, y - 23))
        return rocket_down_img
    elif y_change < 0:
        gameDisplay.blit(rocket_up_img, (x - 25, y - 23))
        return rocket_up_img
    elif y_change == 0 and x_change < 0:
        gameDisplay.blit(rocket_left_img, (x - 25, y - 23))
        return rocket_left_img
    else:
        gameDisplay.blit(rocket_right_img, (x - 25, y - 23))
        return rocket_right_img


def enemy(x, y, kind):
    if kind == "A":
        img = enemyA_img
        gameDisplay.blit(img, (x - 13, y - 13))
    elif kind == "B":
        img = enemyB_img
        gameDisplay.blit(img, (x - 13, y - 13))
    else:
        img = enemyC_img
        gameDisplay.blit(img, (x - 13, y - 13))

def blit_comet(x, y):
    gameDisplay.blit(comet_img, (x - 13, y - 13))


"""def update_figure(figure):
    pygame.draw.rect(gameDisplay, black, (figure.x, figure.y, figure_width, figure_height))

def update_enemy(x_enemy,y_enemy):
    pygame.draw.rect(gameDisplay, red, (x_enemy, y_enemy, 30, 30))"""


def game_loop(spawn_counter, highscore, clock):
    x_change = 0
    y_change = 0
    start = time.time()
    score = 0
    prev_counter = spawn_counter
    enemies = []
    comets = []
    before = rocket_up_img
    not_exit = True
    while not_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0

        gameDisplay.fill(black)
        before = rocket_ship(figure.x, figure.y, x_change, y_change, before)
        pygame.display.update()

        spawn_counter -= 1

        if spawn_counter == prev_counter / 2:
            comets.append(factory.createRandomComet())
        elif prev_counter == 0:
            comets.append(factory.createRandomComet())
            print("amount has reached max")
            spawn_counter = 50

        if spawn_counter == 0:
            enemies.append(factory.createRandomEnemy())
            spawn_counter = prev_counter - 10
            prev_counter = spawn_counter


        if not figure.move(x_change, y_change):
            crash(highscore, score)

        for comet in comets:
            if not comet.move():
                comets.remove(comet)
                continue
            blit_comet(comet.x, comet.y)
            if pygame.Rect.colliderect(
                    pygame.Rect(figure.x, figure.y, figure_width, figure_height),
                    pygame.Rect(comet.x, comet.y, comet_width, comet_height)):
                        crash(highscore, score)

        for foe in enemies:
            if not foe.move():
                enemies.remove(foe)
                continue
            #update_enemy(foe.x, foe.y)
            enemy(foe.x, foe.y, foe.get_kind())
            if pygame.Rect.colliderect(
                    pygame.Rect(figure.x, figure.y, figure_width, figure_height),
                    pygame.Rect(foe.x, foe.y, enemy_width, enemy_height)):
                        crash(highscore, score)

            for comet in comets:
                if pygame.Rect.colliderect(
                        pygame.Rect(foe.x, foe.y, enemy_width, enemy_height),
                        pygame.Rect(comet.x, comet.y, comet_width, comet_height)):
                    enemies.remove(foe)

        font = pygame.font.Font('Futura.ttc', 20)
        gameDisplay.blit(font.render(str(highscore), True, orange), (580, 20))
        score = round(time.time() - start, 3)
        gameDisplay.blit(font.render(str(score), True, orange), (700, 20))
        pygame.display.update()
        clock.tick(60)



game_loop(spawn_counter, highscore, clock)
