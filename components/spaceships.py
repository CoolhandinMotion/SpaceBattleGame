from dataclasses import dataclass, field
from enum import Enum, auto
from components.bullet import default_bullet
from typing import List

from paths import ASSET_PATH
import pygame
from components.config import GameConfig
from collections import namedtuple

spaceship_status = namedtuple('status', ('x', 'y','vel'))
spaceship_size = namedtuple('size', ('width', 'height'))


class SpaceShipType(Enum):
    YELLOW = auto()
    RED = auto()


@dataclass
class Appearance:
    type: SpaceShipType
    rotation: int = 0
    current_width: int = field(init=False)
    current_height: int = field(init=False)
    image: pygame.image = field(init=False)

    def __post_init__(self):
        self.current_width = GameConfig.spaceship_width
        self.current_height = GameConfig.spaceship_height
        if self.type == SpaceShipType.RED:
            self.rotation = 180
        self.load_image()

    def magnify_size(self, magnitude: int) -> None:
        if magnitude <= 5:
            self.current_width = int(self.current_width * magnitude)
            self.current_height = int(self.current_height * magnitude)
            return
        self.current_width = self.current_width * 2
        self.current_height = self.current_height * 2

    def shrink_size(self, div: int) -> None:
        if div <= 5:
            self.current_width = self.current_width // div
            self.current_height = self.current_height // div
            return
        self.current_width = self.current_width // 5
        self.current_height = self.current_height // 5

    def reset_size(self) -> None:
        self.current_width = GameConfig.spaceship_width
        self.current_height = GameConfig.spaceship_height

    def load_image(self) -> None:
        if self.type == SpaceShipType.YELLOW:
            image = pygame.image.load(ASSET_PATH / "spaceship_yellow.png")
            self.image = pygame.transform.scale(image, (self.current_width, self.current_height))
            self.image = pygame.transform.rotate(self.image, self.rotation)
        if self.type == SpaceShipType.RED:
            image = pygame.image.load(ASSET_PATH / "spaceship_red.png")
            self.image = pygame.transform.scale(image, (self.current_width, self.current_height))
            self.image = pygame.transform.rotate(self.image, self.rotation)

    @property
    def size(self):
        return spaceship_size(width=self.current_width, height=self.current_height)


@dataclass
class State:
    x: int
    y: int
    vel: int = GameConfig.space_ship_default_velocity
    health: int = GameConfig.spaceship_default_health
    body: pygame.Rect = field(init=False, repr=False)

    def __post_init__(self):
        self.body = pygame.Rect(self.x,self.y,GameConfig.spaceship_width,GameConfig.spaceship_height)
    def increase_health(self, value: int) -> None:
        self.health = self.health + value

    def decrease_health(self, value: int = 1) -> None:
        if self.health >= value:
            self.health = self.health - value
        self.health = 0

    @property
    def status(self):
        return spaceship_status(x=self.x, y=self.y,vel=self.vel)


@dataclass
class Spaceship:
    appearance: Appearance
    state: State
    bullets_shot: List[pygame.Rect] = field(init=False, default_factory=list)


def shoot(spaceship: Spaceship):
    bullet = default_bullet(spaceship_coordinates=spaceship.state.status,spaceship_size=spaceship.appearance.size)
    spaceship.bullets_shot.append(bullet)