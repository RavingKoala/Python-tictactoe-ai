### todo: CLASS
# 1 TODO: add comments

from . import View


class Controller():
    """Controller class for the Options component"""

    ticTacToe = None

    def __init__(self):
        self.view = View.View(self)

    def initialize(self, MasterFrame):
        self.view.setupGui(MasterFrame)

    def addClasses(self, TicTacToe):
        self.ticTacToe = TicTacToe

    def changeMode(self, Mode):
        self.ticTacToe.checkChangeMode(Mode)

    def resetGame(self):
        self.ticTacToe.resetGame()
