from enum import Enum, auto
from paths import AUDIO_PATH
from components.config import GameConfig
import pygame

pygame.mixer.init()
class SpaceshipType(Enum):
    RED = auto()
    YELLOW = auto()


BULLET_SHOT_SOUND = pygame.mixer.Sound(AUDIO_PATH / "shoot.mp3")
BULLET_HIT_SOUND = pygame.mixer.Sound(AUDIO_PATH / "hit.mp3")


def default_bullet(spaceship_size, spaceship_coordinates):
    bullet = pygame.Rect(spaceship_coordinates.x + spaceship_size.width / 2,
                         spaceship_coordinates.y + spaceship_size.height / 2,
                         GameConfig.bullet_default_size / 2, GameConfig.bullet_default_size / 2)
    return bullet
