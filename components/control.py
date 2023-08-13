from typing import Protocol, Dict

import pygame
from components.navigation import Navigation
from components.spaceships import shoot
from components.spaceships import Spaceship, Appearance, State, SpaceShipType


class NavigationCommand(Protocol):
    def __call__(self, app: Appearance, state: State):
        ...




RED_NAVIGATION_COMMAND: Dict[int, NavigationCommand] = {
    pygame.K_UP: Navigation.move_up,
    pygame.K_DOWN: Navigation.move_down,
    pygame.K_RIGHT: Navigation.move_right,
    pygame.K_LEFT: Navigation.move_left,

}
YELLOW_NAVIGATION_COMMAND: Dict[int, NavigationCommand] = {
    pygame.K_w: Navigation.move_up,
    pygame.K_s: Navigation.move_down,
    pygame.K_d: Navigation.move_right,
    pygame.K_a: Navigation.move_left,

}

RED_SHOOT_COMMAND = {pygame.K_RCTRL: shoot}
YELLOW_SHOOT_COMMAND = {pygame.K_LCTRL: shoot}


def handle_keys_pressed(keys_pressed, red: Spaceship, yellow: Spaceship):
    for command in RED_NAVIGATION_COMMAND:
        if keys_pressed[command]:
            RED_NAVIGATION_COMMAND[command](app=red.appearance, state=red.state)
    for command in YELLOW_NAVIGATION_COMMAND:
        if keys_pressed[command]:
            YELLOW_NAVIGATION_COMMAND[command](app=yellow.appearance, state=yellow.state)
    for command in RED_SHOOT_COMMAND:
        if keys_pressed[command]:
            RED_SHOOT_COMMAND[command](spaceship=red)
    for command in YELLOW_SHOOT_COMMAND:
        if keys_pressed[command]:
            YELLOW_SHOOT_COMMAND[command](spaceship=yellow)
