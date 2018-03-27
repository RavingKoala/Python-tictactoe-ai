### todo: CLASS
# 1 TODO: add comments

from tkinter import Frame, Button
from tkinter import NSEW
from HeadClasses import Component


class MainOptions(Component.HeadComponent):
    ''' Options class
        contains gamemode and restart
    '''

    # predeclaring attributes
    optionsFrame = TTTGame = oneVsOneBtn = monkeyBtn = aiBtn = restartBtn = None

    def addClasses(self, TicTacToeClass):
        self.TTTGame = TicTacToeClass

    def addGui(self, MasterFrame):
        # add options frame
        self.optionsFrame = Frame(MasterFrame, width=1, height=1)
        self.optionsFrame.grid(row=0, column=0, sticky=NSEW)
        self.configureEvenWeight(self.optionsFrame, 6, 3)
        # add 1v1 button
        self.oneVsOneBtn = Button(self.optionsFrame, command=lambda: self.onevOne_onClick(), text='1 v 1', relief='sunken', borderwidth=2, width=10, height=5)
        self.oneVsOneBtn.grid(row=1, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add monkey buttons
        self.monkeyBtn = Button(self.optionsFrame, command=lambda: self.onevsMonkey_onClick(), text='You vs. Monkey', relief='sunken', borderwidth=2, width=10, height=5)
        self.monkeyBtn.grid(row=2, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add ai buttons
        self.aiBtn = Button(self.optionsFrame, command=lambda: self.onevAi_onClick(), text='You vs. AI', relief='sunken', borderwidth=2, width=10, height=5)
        self.aiBtn.grid(row=3, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add restart button
        self.restartBtn = Button(self.optionsFrame, command=lambda: self.restart_onClick(), text='Restart', relief='sunken', borderwidth=2, width=10, height=5)
        self.restartBtn.grid(row=4, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)

    def onevOne_onClick(self):
        self.TTTGame.checkChangeMode(1)

    def onevsMonkey_onClick(self):
        self.TTTGame.checkChangeMode(2)

    def onevAi_onClick(self):
        self.TTTGame.checkChangeMode(3)

    def restart_onClick(self):
        self.TTTGame.resetGame()
