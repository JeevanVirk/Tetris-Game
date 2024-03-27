from tetrominos import Tetromino
from resources.colors import Colors
import pygame

class BombTetromino(Tetromino):
    def __init__(self,tetromino) -> None:
        super().__init__()
        self.blocks = tetromino.blocks
        self.color = tetromino.color
        self.border_color = Colors.YELLOW.value
        
    def draw(self, screen, ui_x_offset, ui_y_offset):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset + 1,
                            (row_index + self.row_offset) * 30 + ui_y_offset + 1,
                            30 - 2,
                            30 - 2,
                        ),
                    )
                    pygame.draw.rect(
                        screen,
                        self.border_color,  # Specify the border color here
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset,
                            (row_index + self.row_offset) * 30 + ui_y_offset,
                            30 - 1,  # Width of the border rectangle
                            30 - 1,  # Height of the border rectangle
                        ),
                    )
                    
    def lock_tetromino(self, game):
        row_offset = self.row_offset - 2 if self.row_offset - 2 != 0 else 0
        column_offset = self.col_offset - 2 if self.col_offset - 2 != 0 else 0
        size = len(self.blocks[self.state])
        for i in range(size + 2):
            if i >= len(game.grid.blocks):
                continue
            for j in range(size + 2):
                if j + row_offset < len(game.grid.blocks[i + row_offset]):
                    game.grid.blocks[j + row_offset][
                        j + column_offset
                        ] = 0