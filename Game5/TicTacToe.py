# todo: CLASS
# 1 TODO:

from tkinter import Frame, Button, Label, messagebox, Toplevel
from tkinter import NSEW
from HeadClasses import Component


class MainTicTacToe(Component.HeadComponent):
    ''' TicTacToe class
        contains the game
    '''

    mode = 1
    buttonsDisabled = False
    # predeclaring attributes
    TTTButtons = []
    TTTFrame = turn = None

    def __init__(self, MainPopupsBool):
        self.PopupsEnabled = MainPopupsBool
        self.setGameState('new')

    def addClasses(self, Turn):
        self.turn = Turn

    def addGui(self, MasterFrame):
        # add TicTacToe frame
        self.TTTFrame = Frame(MasterFrame)
        self.TTTFrame.grid(row=0, column=1, sticky=NSEW)
        self.configureEvenWeight(self.TTTFrame, 3, 3)

        # add the buttons
        for y in range(3):
            for x in range(3):
                self.TTTButtons.append(Button(self.TTTFrame, command=lambda Y=y, X=x: self.TTTBtn_onClick(Y, X), font='calibri 34 bold', text='', relief='groove', borderwidth=3, width=3, height=1))
                self.TTTButtons[y * 3 + x].grid(row=y, column=x, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky=NSEW)

    def setBtnText(self, I, Text):
        self.TTTButtons[I].configure(text=Text)

    def getBtnText(self, I):
        return self.TTTButtons[I]['text']

    def TTTBtn_onClick(self, Y, X):
        self.setGameState('ongoing')
        if self.getBtnText(Y * 3 + X) == '':
            text = self.turn.getCurTurn()
            self.setBtnText(Y * 3 + X, text)
            self.turn.changeTurn()
            self.checkWin()

    def disableButtons(self):
        if not self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for TTTBtn in self.TTTButtons:
                TTTBtn['state'] = 'disabled'

    def enableButtons(self):
        if self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for TTTBtn in self.TTTButtons:
                TTTBtn['state'] = 'active'

    def resetButtons(self):
        for I in range(len(self.TTTButtons)):
            self.setBtnText(I, "")
        self.enableButtons()

    def resetGame(self):
        self.resetButtons()
        self.turn.resetTurn()

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
        for TTTBtn in self.TTTButtons:
            if TTTBtn['text'] == '':
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
            if side == 'horizontal':
                if textList[I * 3] != '':
                    if textList[I * 3] == textList[I * 3 + 1] == textList[I * 3 + 2]:
                        self.doWin(textList[I])
            elif side == 'vertical':
                if textList[I] != '':
                    if textList[I] == textList[I + 3] == textList[I + 6]:
                        self.doWin(textList[I])

    def getAllBtnText(self):
        TTTList = []
        for TTTBtn in self.TTTButtons:
            TTTList.append(TTTBtn['text'])
        return TTTList

    def doWin(self, Player):
        self.endGame()
        if self.PopupsEnabled:
            winner = self.turn.getPlayerName(Player)
            self.doPopupWin(winner)

    @staticmethod
    def doPopupWin(Winner='You'):
        toplevel = Toplevel()
        toplevel.minsize(100, 100)
        label1 = Label(toplevel, text='{0} WON!'.format(Winner))
        label1.grid(sticky=NSEW)

    def endGame(self):
        self.disableButtons()

    def gameStarted(self):
        textList = self.getAllBtnText()
        for labelText in textList:
            if labelText != '':
                return True
        return False

    def setGameState(self, State):
        self.gameState = State

    def checkChangeMode(self, ModeNr):
        if self.gameStarted():
            if self.PopupsEnabled:
                if messagebox.askquestion("Change mode", "Are you sure you want to reset the game?", icon='warning') == 'yes':
                    self.ChangeMode(ModeNr)
            else:
                self.ChangeMode(ModeNr)
        else:
            self.ChangeMode(ModeNr)

    def ChangeMode(self, Mode):
        self.resetGame()
        if self.getMode() != Mode:
            self.setMode(Mode)
            self.turn.setTurnLabel(Mode)
        else:
            return

    def getMode(self):
        return self.mode

    def setMode(self, Mode):
        self.mode = Mode
