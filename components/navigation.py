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
            if state.body.x + app.current_width + state.vel < GAME_WIDTH:
                state.body.x += state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.body.x + app.current_width + state.vel < GAME_WIDTH:
                state.body.x += state.vel
            return

    @staticmethod
    def move_left(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.body.x - state.vel > 0:
                state.body.x -= state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.body.x - state.vel > 0:
                state.body.x -= state.vel
            return

    @staticmethod
    def move_up(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.body.y - state.vel > BORDER_FOR_RED:
                state.body.y -= state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.body.y - state.vel > 0:
                state.body.y -= state.vel
            return

    @staticmethod
    def move_down(app: Appearance, state: State):
        if app.type== SpaceShipType.RED:
            if state.body.y + state.vel + app.current_height < GAME_HEIGHT:
                state.body.y += state.vel
            return

        if app.type== SpaceShipType.YELLOW:
            if state.body.y + app.current_height + state.vel <= BORDER_FOR_YELLOW:
                state.body.y += state.vel
            return
