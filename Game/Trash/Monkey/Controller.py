# todo: CLASS
# 1 TODO:

from random import randint
from time import sleep


class Controller():

    ticTacToe = None

    def addClasses(self, TicTacToeClass):
        self.ticTacToe = TicTacToeClass

    def requestMove(self):
        textList = self.ticTacToe.getAllBtnText()
        print(textList)
        possibilities = {}
        for y, textRow in enumerate(textList):
            for x, textField in enumerate(textRow):
                if textField == "":
                    possibilities[len(possibilities)] = {'Y': y, 'X': x}
        chosenField = randint(0, len(possibilities) - 1)
        sleep(0.5)
        self.ticTacToe.buttonClicked(possibilities[chosenField]['Y'], possibilities[chosenField]['X'])
