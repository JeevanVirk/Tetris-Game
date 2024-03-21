import abc

class PowerTetrominoFactory(abc.ABC):
    @abc.abstractmethod
    def create_power_tetromino(self):
        pass