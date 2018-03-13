# todo -> CLASS
# 1 TODO:

from tkinter import Frame, Label
from tkinter import NSEW
from HeadClasses import Component


class MainTurn(Component.HeadComponent):
    ''' Turn class
        contains data that shows who's turn it is
    '''

    # predeclaring attributes
    player = 'X'
    mode = 1
    turnFrame = XLbl = OLbl = TTTGame = None

    def __init__(self):
        super(MainTurn, self).__init__()

    def addClasses(self, TicTacToe):
        self.TTTGame = TicTacToe

    def addGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnFrame = Frame(MasterFrame, width=1, height=1)
        self.turnFrame.grid(row=0, column=2, sticky=NSEW)
        # set percentage of stretch
        self.configureEvenWeight(self.turnFrame, 8, 3)
        # adds current turn buttons
        self.XLbl = Label(self.turnFrame, text='Player1', background='green2', width=10, height=5)
        self.XLbl.grid(row=3, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)
        self.OLbl = Label(self.turnFrame, text='Player2', background='white', width=10, height=5)
        self.OLbl.grid(row=4, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)

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
            self.XLbl.configure(text='Player')
            self.OLbl.configure(text='AI')

    def resetTurn(self):
        self.setTurnColor('X')
        self.TTTGame.resetButtons()

    def getCurTurn(self):
        return self.player

    def setMode(self, Mode):
        self.TTTGame.resetButtons()
        self.resetTurn()
        if self.mode == 2 and Mode == 1 or self.mode == 1 and Mode == 2:
            self.mode = Mode
            self.setTurnLabel(Mode)
        else:
            return

    def getMode(self):
        return self.mode
