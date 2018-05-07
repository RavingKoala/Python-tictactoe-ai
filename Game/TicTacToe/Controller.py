# todo: CLASS
# 1 TODO: add comments

from . import View
from . import Model
from Interfaces import ControllerInterface
from tkinter import messagebox


class Controller(ControllerInterface.ControllerInterface):
    """Controller class for the TicTacToe component"""

    turn = person = None

    def __init__(self):
        self.view = View.View(self)
        self.model = Model.Model()

    def addClasses(self, Turn):
        self.turn = Turn

    def setSettings(self, PopupsEnabled, TTTDimensions):
        self.view.setSettings(TTTDimensions)
        self.model.setSettings(PopupsEnabled, TTTDimensions)

    def initialize(self, MasterFrame):
        self.view.setupGui(MasterFrame)

    def buttonClicked(self, Y, X):
        print("clicked {0} {1}".format(Y, X))
        if self.model.getBtnText(Y, X) == "":
            text = self.turn.getPlayerIcon()
            self.setBtnText(Y, X, text)
            if self.checkWin():
                self.doWin()
            elif self.checkDraw():
                self.doDraw()
            else:
                self.turn.changeTurn()

    def setBtnText(self, Y, X, Text):
        self.model.setBtnText(Y, X, Text)
        self.view.setBtnText(Y, X, Text)

    def disableButtons(self):
        self.model.setButtonsEnabled(False)
        for y in range(self.model.getDimensions()):
            for x in range(self.model.getDimensions()):
                self.view.disableButton(y, x)

    def enableButtons(self):
        self.model.setButtonsEnabled(True)
        for y in range(self.model.getDimensions()):
            for x in range(self.model.getDimensions()):
                self.view.enableButton(y, x)

    def resetButtonsText(self):
        for y in range(self.model.getDimensions()):
            for x in range(self.model.getDimensions()):
                self.setBtnText(y, x, "")

    def checkWin(self):
        textList = self.model.getAllBtnText()

        def checkBtnRowWin(I, side):
            # check if anybody has won be checking row by row
            if side == 'diagonal':
                if textList[I[0]['y']][I[0]['x']] != "":
                    if textList[I[0]['y']][I[0]['x']] == textList[I[1]['y']][I[1]['x']] == textList[I[2]['y']][I[2]['x']]:
                        return True
            elif side == 'horizontal':
                if textList[I][0] != "":
                    if textList[I][0] == textList[I][1] == textList[I][2]:
                        return True
            elif side == 'vertical':
                if textList[0][I] != "":
                    if textList[0][I] == textList[1][I] == textList[2][I]:
                        return True
            return False

        # check horizontal, vertical, diagonal
        for I in range(self.model.dimensions):
            if checkBtnRowWin(I, 'horizontal') or checkBtnRowWin(I, 'vertical'):
                return True
        if checkBtnRowWin([{'y': 0, 'x': 0}, {'y': 1, 'x': 1}, {'y': 2, 'x': 2}], 'diagonal'):
            return True
        elif checkBtnRowWin([{'y': 0, 'x': 2}, {'y': 1, 'x': 1}, {'y': 2, 'x': 0}], 'diagonal'):
            return True
        return False

    def doWin(self):
        self.endGame()
        if self.model.getPopupsEnabled():
            winner = self.turn.getPlayerName()
            self.doPopup(Type="Win", Text=winner)

    def checkDraw(self):
        for BtnList in self.model.getAllBtnText():
            for BtnText in BtnList:
                if BtnText == "":
                    return False
        return True

    def doDraw(self):
        self.endGame()
        if self.model.getPopupsEnabled():
            self.doPopup(Type="Draw")

    def endGame(self):
        self.disableButtons()

    def gameStarted(self):
        textList = self.model.getAllBtnText()
        for textRow in textList:
            if textRow.count("") < self.model.getDimensions():
                return True
        return False

    def checkChangeMode(self, I):
        if self.model.getPopupsEnabled() and self.gameStarted():
            if messagebox.askquestion("Change mode", "Are you sure you want to reset the game?", icon='warning') == 'yes':
                self.changeMode(I)
        else:
            self.changeMode(I)

    def changeMode(self, I):
        self.resetButtonsText()
        if self.model.getMode() != I:
            self.model.setMode(I)
            self.turn.setMode(I)

    def resetGame(self):
        self.resetButtonsText()
        self.turn.resetTurn()

    def getAllBtnText(self):
        return self.model.getAllBtnText()
