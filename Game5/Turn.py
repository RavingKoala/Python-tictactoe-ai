### todo: CLASS
# 1 TODO: create object containing playeble and name

from tkinter import Frame, Label
from tkinter import NSEW
from HeadClasses import Component


class MainTurn(Component.HeadComponent):
    ''' Turn class
        contains data that shows who's turn it is
    '''

    # predeclaring attributes
    player = 'X'
    turnFrame = XLbl = OLbl = TTTGame = None
    turn = None

    def addClasses(self, TicTacToe):
        self.TTTGame = TicTacToe

    def addGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnFrame = Frame(MasterFrame, width=1, height=1)
        self.turnFrame.grid(row=0, column=2, sticky=NSEW)
        self.configureEvenWeight(self.turnFrame, 6, 3)
        # adds current turn buttons
        self.XLbl = Label(self.turnFrame, text='Player1', background='green2', width=10, height=5)
        self.XLbl.grid(row=2, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)
        self.OLbl = Label(self.turnFrame, text='Player2', background='white', width=10, height=5)
        self.OLbl.grid(row=3, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)

    def toggleColor(self):
        if self.player == 'X':
            self.setTurnColor('O')
        elif self.player == 'O':
            self.setTurnColor('X')

    def toggleTurn(self):
        self.toggleColor()

    def setTurnColor(self, Turn):
        if Turn == 'X':
            self.OLbl.configure(background='white')
            self.XLbl.configure(background='green2')
            self.player = 'X'
        elif Turn == 'O':
            self.XLbl.configure(background='white')
            self.OLbl.configure(background='green2')
            self.player = 'O'

    def setTurnLabel(self, Mode):
        if Mode == 1:
            self.XLbl.configure(text='Player1')
            self.OLbl.configure(text='Player2')
        elif Mode == 2:
            self.XLbl.configure(text='My')
            self.OLbl.configure(text='AI')
        elif Mode == 3:
            self.XLbl.configure(text='AI')
            self.OLbl.configure(text='AI2')

    def getPlayerName(self, player):
        if player == 'X':
            return self.XLbl['text']
        elif player == 'O':
            return self.OLbl['text']
        return 'unknown'

    def resetTurn(self):
        self.setTurnColor('X')

    def getCurTurn(self):
        return self.player

    def setTurn(self, Turn):
        self.turn = Turn

    def updateTurn(self):
        if self.turn == 'My' or self.turn == 'Player1':
            self.TTTGame.enableButtons()
            self.turn.toggleTurn()
        elif self.turn == 'Player2':
            self.TTTGame.enableButtons()
            self.turn.toggleTurn()
        elif self.turn == 'Ai':
            self.TTTGame.disableButtons()
            self.turn.toggleTurn()
        elif self.turn == 'Ai2':
            self.TTTGame.disableButtons()
            self.turn.toggleTurn()

    def changeTurn(self):
        if self.TTTGame.getMode == 1:
            if self.turn == 'My/Player1':
                self.setTurn('Player2')
                self.updateTurn()
            elif self.turn == 'Player2':
                self.setTurn('My/Player1')
                self.updateTurn()
        elif self.TTTGame.getMode == 2:
            if self.turn == 'My/Player1':
                self.setTurn('Ai')
                self.updateTurn()
            elif self.turn == 'Ai':
                self.setTurn('My/Player1')
                self.updateTurn()
        elif self.TTTGame.getMode == 3:
            if self.turn == 'Ai':
                self.setTurn('Ai2')
                self.updateTurn()
            elif self.turn == 'Ai2':
                self.setTurn('Ai')
                self.updateTurn()
