# todo: CLASS
# 1 TODO:

from tkinter import Frame, Button, messagebox
from tkinter import NSEW
from HeadClasses import Component


class MainTicTacToe(Component.HeadComponent):
    ''' TicTacToe class
        contains the game
    '''

    mode = 0
    buttonsDisabled = False
    # predeclaring attributes
    TTTButtons = []
    TTTFrame = turn = None

    def __init__(self, MainPopupsBool):
        self.PopupsEnabled = MainPopupsBool

    def addClasses(self, TurnClass):
        self.turn = TurnClass

    def addGui(self, MasterFrame):
        # add TicTacToe frame
        self.TTTFrame = Frame(MasterFrame)
        self.TTTFrame.grid(row=0, column=1, sticky=NSEW)
        self.configureEvenWeight(self.TTTFrame, 3, 3)

        # add the buttons
        for y in range(3):
            self.TTTButtons.append([])
            for x in range(3):
                self.TTTButtons[y].append(Button(self.TTTFrame, command=lambda Y=y, X=x: self.TTTBtn_onClick(Y, X), font='calibri 34 bold', text="", relief='groove', borderwidth=3, width=3, height=1))
                self.TTTButtons[y][x].grid(row=y, column=x, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky=NSEW)

    def TTTBtn_onClick(self, Y, X):
        if self.getBtnText(Y, X) == "":
            text = self.turn.getPlayerIcon()
            self.setBtnText(Y, X, text)
            if self.checkWin():
                self.doWin()
            elif self.checkDraw():
                self.doDraw()
            self.turn.changeTurn()

    def setBtnText(self, Y, X, Text):
        self.TTTButtons[Y][X].configure(text=Text)

    def getBtnText(self, Y, X):
        return self.TTTButtons[Y][X]['text']

    def disableButtons(self):
        if not self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for y in range(len(self.TTTButtons)):
                for TTTBtn in self.TTTButtons[y]:
                    TTTBtn.config(state="disabled")

    def enableButtons(self):
        if self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for y in range(len(self.TTTButtons)):
                for TTTBtn in self.TTTButtons[y]:
                    TTTBtn.config(state="normal")

    def resetButtonsText(self):
        for y in range(len(self.TTTButtons)):
            for x in range(len(self.TTTButtons[y])):
                self.setBtnText(y, x, "")

    def checkWin(self):
        textList = self.getAllBtnText()

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
        for I in range(len(self.TTTButtons)):
            if checkBtnRowWin(I, 'horizontal') or checkBtnRowWin(I, 'vertical'):
                return True
        if checkBtnRowWin([{'y': 0, 'x': 0}, {'y': 1, 'x': 1}, {'y': 2, 'x': 2}], 'diagonal'):
            return True
        elif checkBtnRowWin([{'y': 0, 'x': 2}, {'y': 1, 'x': 1}, {'y': 2, 'x': 0}], 'diagonal'):
            return True
        return False

    def doWin(self):
        self.endGame()
        if self.PopupsEnabled:
            # if self.mode ==
            winner = self.turn.getPlayerName()
            self.doPopup(Type="Win", Text=winner)

    def checkDraw(self):
        for y in range(len(self.TTTButtons)):
            for TTTBtn in self.TTTButtons[y]:
                if TTTBtn['text'] == "":
                    return False
        return True

    def doDraw(self):
        self.endGame()
        self.doPopup(Type="Draw")

    def getAllBtnText(self):
        textList = []
        for y in range(len(self.TTTButtons)):
            textList.append([])
            for TTTBtn in self.TTTButtons[y]:
                textList[y].append(TTTBtn['text'])
        return textList

    def endGame(self):
        self.disableButtons()

    def gameStarted(self):
        textList = self.getAllBtnText()
        for textRow in textList:
            for labelText in textRow:
                if labelText != "":
                    return True
        return False

    def checkChangeMode(self, ModeNr):
        if self.PopupsEnabled and self.gameStarted():
            if messagebox.askquestion("Change mode", "Are you sure you want to reset the game?", icon='warning') == 'yes':
                self.ChangeMode(ModeNr)
            self.ChangeMode(ModeNr)
        self.ChangeMode(ModeNr)

    def ChangeMode(self, Mode):
        self.resetGame()
        if self.getMode() != Mode:
            self.setMode(Mode)
            self.turn.setMode(Mode)
        else:
            return

    def resetGame(self):
        self.resetButtonsText()
        self.turn.resetTurn()
        self.enableButtons()

    def getMode(self):
        return self.mode

    def setMode(self, Mode):
        self.mode = Mode
