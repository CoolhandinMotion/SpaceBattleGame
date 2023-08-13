from enum import Enum, auto

from components.config import GameConfig
import pygame


class SpaceshipType(Enum):
    RED = auto()
    YELLOW = auto()


def default_bullet(spaceship_size, spaceship_coordinates):
    bullet = pygame.Rect(spaceship_coordinates.x + spaceship_size.width / 2,
                         spaceship_coordinates.y + spaceship_size.height / 2,
                         GameConfig.bullet_default_size / 2, GameConfig.bullet_default_size / 2)
    return bullet


