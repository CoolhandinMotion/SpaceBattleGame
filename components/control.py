from enum import Enum, auto
from typing import Protocol, Dict
from components.config import GameConfig
import pygame
from components.navigation import Navigation
from components.spaceships import Spaceship, Appearance, State, shoot
from components.events import RED_IS_HIT, YELLOW_IS_HIT, WE_HAVE_A_WINNER


class SpaceshipType(Enum):
    RED = auto()
    YELLOW = auto()


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


def handle_navigation_keys_pressed(keys_pressed, red: Spaceship, yellow: Spaceship):
    for command in RED_NAVIGATION_COMMAND:
        if keys_pressed[command]:
            RED_NAVIGATION_COMMAND[command](app=red.appearance, state=red.state)
    for command in YELLOW_NAVIGATION_COMMAND:
        if keys_pressed[command]:
            YELLOW_NAVIGATION_COMMAND[command](app=yellow.appearance, state=yellow.state)


def handle_shooting_events(event: pygame.event, red: Spaceship, yellow: Spaceship):
    if event.type == pygame.KEYDOWN and event.key in RED_SHOOT_COMMAND:
        RED_SHOOT_COMMAND[event.key](red)
    if event.type == pygame.KEYDOWN and event.key in YELLOW_SHOOT_COMMAND:
        YELLOW_SHOOT_COMMAND[event.key](yellow)


def handle_bullets_shot_movements(red: Spaceship, yellow: Spaceship):
    for bullet in red.bullets_shot:
        bullet.y -= GameConfig.bullet_default_velocity
        if bullet.y < 0:
            red.bullets_shot.remove(bullet)
    for bullet in yellow.bullets_shot:
        bullet.y += GameConfig.bullet_default_velocity
        if bullet.y > GameConfig.height:
            yellow.bullets_shot.remove(bullet)


def handle_bullet_hit(red: Spaceship, yellow: Spaceship):
    for bullet in red.bullets_shot:
        if yellow.state.body.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_IS_HIT))
            red.bullets_shot.remove(bullet)
    for bullet in yellow.bullets_shot:
        if red.state.body.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_IS_HIT))
            yellow.bullets_shot.remove(bullet)


def handle_winner(red: Spaceship, yellow: Spaceship):
    if red.state.health == 0 or yellow.state.health == 0:
        pygame.event.post(pygame.event.Event(WE_HAVE_A_WINNER))
