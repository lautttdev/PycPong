import pygame

from player import Player
from marker import Marker
from ball import Ball

pygame.init()

SIZE = WIDTH, HEIGHT = (800, 600)
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
DELTA = 0

PLAYERS_GROUP = pygame.sprite.Group()
BALL_GROUP = pygame.sprite.Group()

MARKER = Marker(SCREEN)

PLAYER_ONE = Player(PLAYERS_GROUP, 1, SCREEN)
PLAYER_TWO = Player(PLAYERS_GROUP, 2, SCREEN)
BALL = Ball(BALL_GROUP, PLAYERS_GROUP, SCREEN, MARKER)

BACKGROUND_LINE = pygame.Surface((6.7, HEIGHT - 100))
BACKGROUND_LINE.fill("white")

in_process = True


def draw_all():
    SCREEN.fill("black")
    SCREEN.blit(BACKGROUND_LINE, BACKGROUND_LINE.get_rect(center=(WIDTH / 2, HEIGHT / 2)))

    PLAYERS_GROUP.draw(SCREEN)
    BALL_GROUP.draw(SCREEN)


def update():
    PLAYERS_GROUP.update(delta=DELTA)
    BALL_GROUP.update(delta=DELTA)
    MARKER.update()


def on_ready():
    pygame.time.wait(1500)


while in_process:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_process = False

    draw_all()
    update()

    DELTA = CLOCK.tick(60) / 1000
    pygame.display.flip()


pygame.quit()