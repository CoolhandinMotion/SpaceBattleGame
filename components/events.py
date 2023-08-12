from typing import Callable, Dict, Protocol
import pygame
from components.navigation import Navigation
from dataclasses import dataclass

# @dataclass
# class State(Protocol):
#     x: int
#     y: int
#     vel: int
#
#
# @dataclass
# class Appearance(Protocol):
#     current_width: int
#     current_height: int
#
#
# @dataclass
# class Spaceship(Protocol):
#     appearance: Appearance
#     navigation: Navigation





def handle_events(event):
    handle_quit_game(event)


def handle_quit_game(event: pygame.event):
    if event.type == pygame.QUIT:
        quit()
    return



