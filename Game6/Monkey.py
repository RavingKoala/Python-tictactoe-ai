### todo: CLASS
# 1 TODO: add comments
from random import randint
from time import sleep


class MainMonkey():
    TTTGame = None

    def addClasses(self, TicTacToeClass):
        self.TTTGame = TicTacToeClass

    def requestMove(self):
        textList = self.TTTGame.getAllBtnText()
        possibilities = {}
        for y, textRow in enumerate(textList):
            for x, textField in enumerate(textRow):
                if textField == "":
                    possibilities[len(possibilities)] = {'Y': y, 'X': x}
        print(possibilities)
        chosenField = randint(0, len(possibilities) - 1)
        sleep(0.5)
        self.TTTGame.TTTBtn_onClick(possibilities[chosenField]['Y'], possibilities[chosenField]['X'])
