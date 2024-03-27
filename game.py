import random
import pygame
from command import Command
from grid import Grid
from resources.ui import UI
from freezepowerupfactory import FreezePowerupFactory
from bombpowerupfactory import BombPowerupFactory
from tetrominos import (
    ITetromino,
    OTetromino,
    ZTetromino,
    TTetromino,
    STetromino,
    JTetromino,
    LTetromino,
)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (500, 620)
        )  # set the screen size to 300x600 . 20rowsx10columns grid. Each cell is 30x30 pixels
        self.game_over = False
        self.score = 0

        # game objects
        self.grid = Grid()
        self.freeze_now = False
        self.bomb_now = False
        self.tetromino = self.spawn_new_tetromino()
        self.ui = UI()
        self.next_tetromino = self.spawn_new_tetromino()
        

    def run(self):

        event_every_200ms = pygame.USEREVENT + 1
        pygame.time.set_timer(event_every_200ms, 200)

        while True:
            command = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_over == True:
                        self.__init__()
                    if event.key == pygame.K_LEFT and self.game_over == False:
                        command = Command.LEFT
                    if event.key == pygame.K_RIGHT and self.game_over == False:
                        command = Command.RIGHT
                    if event.key == pygame.K_DOWN and self.game_over == False:
                        command = Command.DOWN
                        # self.update_score(0, 1)
                    if event.key == pygame.K_UP and self.game_over == False:
                        command = Command.UP
                    if event.key == pygame.K_f and self.game_over == False:
                        self.freeze_now  = True
                    if event.key == pygame.K_b and self.game_over == False:
                        bomb = BombPowerupFactory().create_power_tetromino(self.tetromino)
                        bomb.row_offset = self.tetromino.row_offset
                        bomb.col_offset = self.tetromino.col_offset
                        bomb.state = self.tetromino.state
                        bomb.color = self.tetromino.color
                        self.tetromino = bomb
                        
                elif event.type == event_every_200ms and self.game_over == False:
                    command = Command.DOWN
                    
                if self.freeze_now == True:
                     pygame.time.set_timer(event_every_200ms, 2000)
                else:
                     pygame.time.set_timer(event_every_200ms, 200)
                    

            self.update(command)
            self.draw()
            pygame.display.update()
            

    def draw(self):
        self.ui.draw(self.screen, self)
        self.grid.draw(self.screen, 10, 10)
        self.tetromino.draw(self.screen, 10, 10)

    def update(self, command):
        self.tetromino.update(command, self)
        
    def spawn_new_tetromino(self):
        self.freeze_now = False
    
        random_value  = random.randint(1, 100)
        print(random_value)
             # Check if the score reaches 50 to spawn the Bomb power-up Tetromino
        if random_value >= 90 or self.bomb_now == True:
            print("Hello")
            self.bomb_now = False
                # Spawn the Bomb power-up Tetromino
            print(self.tetromino,"L")
            return BombPowerupFactory().create_power_tetromino(self.tetromino)

            # Check if the score reaches 100 to spawn the Freeze power-up Tetromino
        if random_value <= 15:
            self.freeze_now = True
                # Spawn the Freeze power-up Tetromino
            print(self.tetromino,"J")
            return FreezePowerupFactory().create_power_tetromino(self.tetromino)
        if random_value > 15 and random_value < 90:
            return random.choice(
                [
                    TTetromino(),
                    ITetromino(),
                    OTetromino(),
                    ZTetromino(),
                    STetromino(),
                    JTetromino(),
                    LTetromino(),
                ]
            )

    def check_for_any_full_lines_to_clear(self):
        return self.grid.check_for_any_full_lines_to_clear()
    
    def update_score(self, lined_cleared, move_down_points):
        self.score += move_down_points
        if lined_cleared == 1:
            self.score += 100
        if lined_cleared == 2:
            self.score += 300
        if lined_cleared == 3:
            self.score += 500
