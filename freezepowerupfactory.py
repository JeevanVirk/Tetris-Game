from powertetrominofactory import PowerTetrominoFactory
from tetrominos import Tetromino
from freezetetromino import FreezeTetromino

class FreezePowerupFactory(PowerTetrominoFactory):
    def create_power_tetromino(self,tetromino):
         return FreezeTetromino(tetromino)