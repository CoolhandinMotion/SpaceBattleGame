from collections import namedtuple
from dataclasses import dataclass
import pygame
from typing import Protocol, Tuple
from components.config import GameConfig
from components.spaceships import Spaceship, Appearance, State

spaceship_status = namedtuple('status', ('x', 'y', 'vel'))


def set_caption():
    pygame.display.set_caption(GameConfig.game_caption)


def initiate_game_window() -> pygame.display:
    game_window = pygame.display.set_mode((GameConfig.width, GameConfig.height))
    return game_window


def draw_border(window: pygame.display):
    border = pygame.Rect(0, GameConfig.height / 2 - GameConfig.border_width / 2, GameConfig.width,
                         GameConfig.border_width)
    pygame.draw.rect(window, GameConfig.border_color, border)


def draw_bullet(window: pygame.display, bullet: pygame.Rect):
    pygame.draw.rect(window, GameConfig.default_bullet_color, bullet)


def draw_bullets_shot(window: pygame.display, red: Spaceship, yellow: Spaceship):
    for bullet in red.bullets_shot:
        draw_bullet(window, bullet)
    for bullet in yellow.bullets_shot:
        draw_bullet(window, bullet)


def draw_spaceship(window: pygame.display, spaceship_img: pygame.display, spaceship_coordinates: State.status):
    window.blit(spaceship_img, (spaceship_coordinates.x, spaceship_coordinates.y))


def draw_game_window(window: pygame.display, red: Spaceship, yellow: Spaceship):
    window.fill(GameConfig.background_color)
    draw_border(window)
    draw_spaceship(window, yellow.appearance.image, yellow.state.status)
    draw_spaceship(window, red.appearance.image, red.state.status)
    draw_bullets_shot(window,red=red,yellow=yellow)
    pygame.display.update()
