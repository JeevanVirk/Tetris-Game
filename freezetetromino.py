from tetrominos import Tetromino,JTetromino,LTetromino,OTetromino,STetromino,TTetromino,ZTetromino
from resources.colors import Colors
import pygame
import random

class FreezeTetromino(Tetromino):
    def __init__(self,tetromino) -> None:
        super().__init__()
        self.blocks = tetromino.blocks
        self.color = tetromino.color
        self.border_color = Colors.WHITE.value
        
    def draw(self, screen, ui_x_offset, ui_y_offset):
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
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
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset + 1,
                            (row_index + self.row_offset) * 30 + ui_y_offset + 1,
                            30 - 3,
                            30 - 3,
                        ),
                   )
   
      
    
