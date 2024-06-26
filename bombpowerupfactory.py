from powertetrominofactory import PowerTetrominoFactory
from tetrominos import Tetromino
from bombtetromino import BombTetromino

class BombPowerupFactory(PowerTetrominoFactory):
    
    def create_power_tetromino(self,tetromino):    
        return BombTetromino(tetromino)
    