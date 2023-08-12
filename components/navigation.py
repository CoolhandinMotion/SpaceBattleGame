from components.config import GameConfig
from components.spaceships import SpaceShipType,Appearance,State

GAME_WIDTH = GameConfig.width
GAME_HEIGHT = GameConfig.height
BORDER_FOR_RED = int(GameConfig.height / 2 + GameConfig.border_width / 2)
BORDER_FOR_YELLOW = int(GameConfig.height / 2 - GameConfig.border_width / 2)


class Navigation:

    @staticmethod
    def move_right(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.x + app.current_width + state.vel < GAME_WIDTH:
                state.x += state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.x + app.current_width + state.vel < GAME_WIDTH:
                state.x += state.vel
            return

    @staticmethod
    def move_left(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.x - state.vel > 0:
                state.x -= state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.x - state.vel > 0:
                state.x -= state.vel
            return

    @staticmethod
    def move_up(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.y - state.vel > BORDER_FOR_RED:
                state.y -= state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.y - state.vel > 0:
                state.y -= state.vel
            return

    @staticmethod
    def move_down(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.y + state.vel + app.current_height < GAME_HEIGHT:
                state.y += state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.y + app.current_height + state.vel <= BORDER_FOR_YELLOW:
                state.y += state.vel
            return
