import components.view as view
import pygame
from components.config import GameConfig
from components.events import handle_events
import components.spaceships as spaceship
from components.control import handle_navigation_keys_pressed, handle_bullets_shot_movements,handle_shooting_events,\
    handle_bullet_hit, handle_winner



WIN = view.initiate_game_window()
view.set_caption()


def main():
    run = True
    clock = pygame.time.Clock()
    yellow_app = spaceship.Appearance(spaceship.SpaceShipType.YELLOW)
    yellow_state = spaceship.State(x=GameConfig.yellow_spaceship_x, y=GameConfig.yellow_spaceship_y)
    yellow = spaceship.Spaceship(appearance=yellow_app, state=yellow_state)

    red_app = spaceship.Appearance(spaceship.SpaceShipType.RED)
    red_state = spaceship.State(x=GameConfig.red_spaceship_x, y=GameConfig.red_spaceship_y)
    red = spaceship.Spaceship(appearance=red_app, state=red_state)

    while run:
        clock.tick(GameConfig.fps)

        game_events = pygame.event.get()
        for event in game_events:
            handle_events(event, red, yellow)
            handle_shooting_events(event,red, yellow)

        keys_pressed = pygame.key.get_pressed()
        handle_navigation_keys_pressed(keys_pressed, red=red, yellow=yellow)
        handle_bullets_shot_movements(red=red,yellow=yellow)
        handle_bullet_hit(red, yellow)
        handle_winner(red, yellow)
        view.draw_game_window(WIN, yellow=yellow, red=red)


if __name__ == '__main__':
    main()
