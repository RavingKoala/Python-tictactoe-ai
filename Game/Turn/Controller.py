from . import View
from . import Model
from Interfaces import ControllerInterface
from random import randint


class Controller(ControllerInterface.ControllerInterface):
    """Controller class for the Turn component"""

    ticTacToe = monkey = ai = None

    def __init__(self):
        self.view = View.View(self)
        self.model = Model.Model()

    def addClasses(self, TicTacToe, Player):
        self.ticTacToe = TicTacToe
        self.player = Player

    def initialize(self, MasterFrame):
        self.view.setupGui(MasterFrame)
