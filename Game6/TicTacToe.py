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
            self.TTTButtons.append([])
            for x in range(3):
                self.TTTButtons[y].append(Button(self.TTTFrame, command=lambda Y=y, X=x: self.TTTBtn_onClick(Y, X), font='calibri 34 bold', text='', relief='groove', borderwidth=3, width=3, height=1))
                self.TTTButtons[y][x].grid(row=y, column=x, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky=NSEW)

    def setBtnText(self, Y, X, Text):
        self.TTTButtons[Y][X].configure(text=Text)

    def getBtnText(self, Y, X):
        return self.TTTButtons[Y][X]['text']

    def TTTBtn_onClick(self, Y, X):
        self.setGameState('ongoing')
        if self.getBtnText(Y, X) == '':
            text = self.turn.getTurn()
            self.setBtnText(Y, X, text)
            self.turn.changeTurn()
            self.checkWin()

    def disableButtons(self):
        if not self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for y in range(len(self.TTTButtons)):
                for TTTBtn in self.TTTButtons[y]:
                    TTTBtn['state'] = 'disabled'

    def enableButtons(self):
        if self.buttonsDisabled:
            self.buttonsDisabled = not self.buttonsDisabled
            for TTTBtn in self.TTTButtons:
                TTTBtn['state'] = 'active'

    def resetButtons(self):
        for y in range(len(self.TTTButtons)):
            for x in range(len(self.TTTButtons[y])):
                self.setBtnText(y, x, "")

    def resetGame(self):
        self.enableButtons()
        self.resetButtons()
        self.turn.resetTurn()

    def checkWin(self):
        # check horizontal, vertical, diagonal
        for I in range(len(self.TTTButtons)):
            self.checkBtnRowWin(I, 'vertical')
            self.checkBtnRowWin(I, 'horizontal')
        self.checkBtnRowWin([{'y': 0, 'x': 0}, {'y': 1, 'x': 1}, {'y': 2, 'x': 2}], 'diagonal')
        self.checkBtnRowWin([{'y': 0, 'x': 2}, {'y': 1, 'x': 1}, {'y': 2, 'x': 0}], 'diagonal')
        if self.isdraw():
            self.doDraw()

    def doDraw(self):
        self.endGame()

    def isdraw(self):
        for y in range(len(self.TTTButtons)):
            for TTTBtn in self.TTTButtons[y]:
                if TTTBtn['text'] == '':
                    return False
        return True

    def checkBtnRowWin(self, I, side):
        textList = self.getAllBtnText()
        # algaritme to check if row is
        if side == 'diagonal':
            if textList[I[0]['y']][I[0]['x']] != '':
                if textList[I[0]['y']][I[0]['x']] == textList[I[1]['y']][I[1]['x']] == textList[I[2]['y']][I[2]['x']]:
                    self.doWin(textList[I[0]['y']][I[0]['x']])
        elif side == 'horizontal':
            if textList[I][0] != '':
                if textList[I][0] == textList[I][1] == textList[I][2]:
                    self.doWin(textList[I][0])
        elif side == 'vertical':
            if textList[0][I] != '':
                if textList[0][I] == textList[1][I] == textList[2][I]:
                    self.doWin(textList[0][I])

    def getAllBtnText(self):
        textList = []
        for y in range(len(self.TTTButtons)):
            textList.append([])
            for TTTBtn in self.TTTButtons[y]:
                textList[y].append(TTTBtn['text'])
        return textList

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
