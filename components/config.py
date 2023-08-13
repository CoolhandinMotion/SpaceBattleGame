from dataclasses import dataclass
from typing import Tuple
import pygame


@dataclass
class GameConfig:
    width: int = 900
    height: int = 600
    fps: int = 60
    background_color: int =(240, 221, 80)
    border_color: Tuple[int, int, int] = (220, 10, 0)
    default_bullet_color: Tuple[int,int,int] =(255, 0, 0)
    border_width: int = 10
    spaceship_width: int = 55
    spaceship_height: int = 40
    space_ship_default_velocity: int = 7
    yellow_spaceship_x: int = 400
    yellow_spaceship_y: int = 100
    red_spaceship_x: int = 400
    red_spaceship_y: int = 500
    spaceship_default_health: int =5
    spaceship_max_bullet: int =3
    bullet_default_velocity: int = 10
    bullet_default_size: int = 10
    game_caption: str = "This is Spaceship battle!!"







