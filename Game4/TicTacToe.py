# todo -> CLASS
# 1 TODO:

from tkinter import Frame, Button
from tkinter import NSEW
from math import floor
from HeadClasses import Component


class MainTicTacToe(Component.HeadComponent):
    ''' TicTacToe class
        contains the game
    '''

    # predeclaring attributes
    TTTButtons = []
    TTTFrame = None
    Turn = None

    def __init__(self, MainPopupsBool):
        # running init from parent class
        super(MainTicTacToe, self).__init__()
        self.PopupsEnabled = MainPopupsBool

    def addClasses(self, Turn):
        self.Turn = Turn

    def addGui(self, MasterFrame):
        # add TicTacToe frame
        self.TTTFrame = Frame(MasterFrame)
        self.TTTFrame.grid(row=0, column=1, sticky=NSEW)
        # set percentage of stretch
        self.configureEvenWeight(self.TTTFrame, 3, 3)

        # add the buttons
        for I in range(9):
            self.TTTButtons.append(Button(self.TTTFrame, command=lambda nr=I: self.onClick(nr), font='calibri 34 bold', text='', relief='groove', borderwidth=3, width=3, height=1))
            rowI = floor(I / 3)
            columnI = floor(I % 3)
            self.TTTButtons[I].grid(row=rowI, column=columnI, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky=NSEW)

    def setBtnText(self, I, Text):
        self.TTTButtons[I].configure(text=Text)

    def getBtnText(self, I):
        return self.TTTButtons[I]['text']

    def onClick(self, I):
        if self.getBtnText(I) == '':
            text = self.Turn.getCurTurn()
            self.setBtnText(I, text)
            self.Turn.toggleTurn()
            self.checkWin()

    def resetButtons(self):
        for I in range(9):
            self.setBtnText(I, "")
            self.TTTButtons[I]['state'] = 'active'

    def checkWin(self):
        # check horizontal, vertical, diagonal
        for I in range(3):
            self.checkBtnRowWin(I, 'vertical')
            self.checkBtnRowWin(I, 'horizontal')
        self.checkBtnRowWin([2, 4, 6], 'diagonal')
        self.checkBtnRowWin([0, 4, 8], 'diagonal')
        if self.isdraw():
            self.doDraw()

    def doDraw(self):
        self.endGame()

    def isdraw(self):
        for I in range(9):
            if self.TTTButtons[I]['text'] == '':
                return False
        return True

    def checkBtnRowWin(self, I, side):
        textList = self.getAllBtnText()
        # algaritme to check if row is
        if side == 'diagonal':
            if textList[I[0]] != '':
                if textList[I[0]] == textList[I[1]] == textList[I[2]]:
                    self.doWin(textList[I[0]])
        else:
            if textList[I] != '':
                if side == 'horizontal':
                    if textList[I] == textList[I + 1] == textList[I + 2]:
                        self.doWin(textList[I])
                elif side == 'vertical':
                    if textList[I] == textList[I + 3] == textList[I + 6]:
                        self.doWin(textList[I])

    def getAllBtnText(self):
        TTTList = []
        for tempI in range(9):
            TTTList.append(self.TTTButtons[tempI]['text'])
        return TTTList

    def doWin(self, PlayerNr):
        self.endGame()
        if self.PopupsEnabled:
            if self.Turn.getMode() == 1:  # 1vs1
                pass
            if self.Turn.getMode() == 2:  # PvsAI
                pass

    def endGame(self):
        for I in range(9):
            self.TTTButtons[I]['state'] = 'disabled'

    def GameStarted(self):
        textList = self.getAllBtnText()
        for labelText in textList:
            if labelText != '':
                return True
        return False
