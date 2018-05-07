from . import Model
from Interfaces import ControllerInterface
from random import randint


class Controller(ControllerInterface.ControllerInterface):
    """Controller class for the Turn component"""

    ticTacToe = None

    def __init__(self):
        self.model = Model.Model()

    def addClasses(self, TicTacToe):
        self.ticTacToe = TicTacToe
