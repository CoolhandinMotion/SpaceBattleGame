from typing import Callable, Dict, Protocol
import pygame
from components.navigation import Navigation
from dataclasses import dataclass

YELLOW_IS_HIT = pygame.USEREVENT + 1
RED_IS_HIT = pygame.USEREVENT + 2

def handle_events(event):
    handle_quit_game(event)


def handle_quit_game(event: pygame.event):
    if event.type == pygame.QUIT:
        quit()
    return





