import components.view
from components.bullet import BULLET_HIT_SOUND
import pygame
from components.spaceships import Spaceship

YELLOW_IS_HIT = pygame.USEREVENT + 1
RED_IS_HIT = pygame.USEREVENT + 2
WE_HAVE_A_WINNER = pygame.USEREVENT + 3


def handle_events(event, red: Spaceship, yellow: Spaceship):
    handle_quit_game(event)
    if event.type == RED_IS_HIT:
        red.state.decrease_health()
        BULLET_HIT_SOUND.play()
    if event.type == YELLOW_IS_HIT:
        yellow.state.decrease_health()
        BULLET_HIT_SOUND.play()



def handle_quit_game(event: pygame.event):
    if event.type == pygame.QUIT:
        quit()
    return


