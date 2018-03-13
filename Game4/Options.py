# todo -> CLASS
# 1 TODO:

from tkinter import Frame, Button, messagebox
from tkinter import NSEW
from HeadClasses import Component


class MainOptions(Component.HeadComponent):
    ''' Options class
        contains gamemode and restart
    '''

    # predeclaring attributes
    optionsFrame = None
    oneVsOneBtn = None
    aiBtn = None
    restartBtn = None
    TTTGame = None
    Turn = None

    def __init__(self, PopupsBool):
        # running init from parent class
        super(MainOptions, self).__init__()
        self.PopupsEnabled = PopupsBool

    def addClasses(self, Turn, TicTacToe):
        self.TTTGame = TicTacToe
        self.Turn = Turn

    def addGui(self, MasterFrame):
        # add options frame
        self.optionsFrame = Frame(MasterFrame, width=1, height=1)
        self.optionsFrame.grid(row=0, column=0, sticky=NSEW)
        # set percentage of stretch
        self.configureEvenWeight(self.optionsFrame, 5, 3)
        # add 1v1 button
        self.oneVsOneBtn = Button(self.optionsFrame, command=lambda: self.onevOne_onClick(), text='1 v 1', relief='sunken', borderwidth=2, width=10, height=5)
        self.oneVsOneBtn.grid(row=1, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add ai button
        self.aiBtn = Button(self.optionsFrame, command=lambda: self.onevAi_onClick(), text='Play vs. AI', relief='sunken', borderwidth=2, width=10, height=5)
        self.aiBtn.grid(row=2, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add restart button
        self.restartBtn = Button(self.optionsFrame, command=lambda: self.restart_onClick(), text='Restart', relief='sunken', borderwidth=2, width=10, height=5)
        self.restartBtn.grid(row=3, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)

    def onevOne_onClick(self):
        self.ChangeMode(1)

    def onevAi_onClick(self):
        self.ChangeMode(2)

    def ChangeMode(self, ModeNr):
        if self.TTTGame.GameStarted():
            if self.PopupsEnabled:
                if messagebox.askquestion("Change mode", "Are you sure you want to reset the game?", icon='warning') == 'yes':
                    self.Turn.setMode(ModeNr)
            else:
                self.Turn.setMode(ModeNr)

    def restart_onClick(self):
        self.Turn.resetTurn()
