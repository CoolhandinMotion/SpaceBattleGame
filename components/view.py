from collections import namedtuple
from dataclasses import dataclass
import pygame
from typing import Protocol, Tuple
from components.config import GameConfig
from components.spaceships import Spaceship, Appearance, State

spaceship_status = namedtuple('status', ('x', 'y', 'vel'))
pygame.font.init()
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)


def set_caption():
    pygame.display.set_caption(GameConfig.game_caption)


def initiate_game_window() -> pygame.display:
    game_window = pygame.display.set_mode((GameConfig.width, GameConfig.height))
    return game_window


def draw_border(window: pygame.display):
    border = pygame.Rect(0, GameConfig.height / 2 - GameConfig.border_width / 2, GameConfig.width,
                         GameConfig.border_width)
    pygame.draw.rect(window, GameConfig.border_color, border)


def draw_bullets_shot(window: pygame.display, red: Spaceship, yellow: Spaceship):
    for bullet in red.bullets_shot:
        pygame.draw.rect(window, GameConfig.default_bullet_color, bullet)
    for bullet in yellow.bullets_shot:
        pygame.draw.rect(window, GameConfig.default_bullet_color, bullet)


def draw_spaceship(window: pygame.display, spaceship_img: pygame.display, spaceship_coordinates: State.status):
    window.blit(spaceship_img, (spaceship_coordinates.x, spaceship_coordinates.y))


def draw_spaceship_health_text(window: pygame.display, status: State, coordinates: Tuple[int, int]):
    health_text = HEALTH_FONT.render("Health : " + str(status.health), True, (0, 0, 0))
    window.blit(health_text, coordinates)


def draw_winner_announcement(window: pygame.display, red: Spaceship, yellow: Spaceship):
    if red.state.health != 0 and yellow.state.health != 0:
        return
    text = ""
    if red.state.health == 0:
        text = "Yellow wins !!!"
    if yellow.state.health == 0:
        text = "Red wins !!!"
    draw_text = WINNER_FONT.render(text, 1, (0, 0, 0))
    window.blit(draw_text,
                (GameConfig.width / 2 - draw_text.get_width() / 2, GameConfig.height / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_game_window(window: pygame.display, red: Spaceship, yellow: Spaceship):
    window.fill(GameConfig.background_color)
    draw_border(window)
    draw_spaceship(window, yellow.appearance.image, yellow.state.status)
    draw_spaceship(window, red.appearance.image, red.state.status)
    draw_spaceship_health_text(window, status=red.state, coordinates=(2, int(GameConfig.height / 2 + 5)))
    draw_spaceship_health_text(window, status=yellow.state, coordinates=(2, 5))
    draw_bullets_shot(window, red=red, yellow=yellow)
    draw_winner_announcement(window, red, yellow)
    pygame.display.update()
