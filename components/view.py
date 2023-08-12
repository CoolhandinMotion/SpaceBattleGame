from collections import namedtuple
from dataclasses import dataclass
import pygame
from typing import Protocol, Tuple
from components.config import GameConfig

spaceship_status = namedtuple('status', ('x', 'y', 'vel'))


class State(Protocol):
    x: int
    y: int
    vel: int

    @property
    def status(self):
        return spaceship_status(x=self.x, y=self.y, vel=self.vel)


class Appearance(Protocol):
    image: pygame.image


class Spaceship(Protocol):
    appearance: Appearance
    state: State

def set_caption():
    pygame.display.set_caption(GameConfig.game_caption)

def initiate_game_window() -> pygame.display:
    game_window = pygame.display.set_mode((GameConfig.width, GameConfig.height))
    return game_window


def draw_border(window: pygame.display):
    border = pygame.Rect(0, GameConfig.height / 2 - GameConfig.border_width / 2, GameConfig.width,
                         GameConfig.border_width)
    pygame.draw.rect(window, GameConfig.border_color, border)


# def draw_bullets(bullet_):



def draw_spaceship(window: pygame.display, spaceship_img: pygame.display, spaceship_coordinates: State.status):
    window.blit(spaceship_img, (spaceship_coordinates.x, spaceship_coordinates.y))


def draw_game_window(window: pygame.display, red: Spaceship, yellow: Spaceship):
    window.fill(GameConfig.background_color)
    draw_border(window)
    draw_spaceship(window, yellow.appearance.image, yellow.state.status)
    draw_spaceship(window, red.appearance.image, red.state.status)
    pygame.display.update()
