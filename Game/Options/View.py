### todo: CLASS
# 1 TODO: add comments

from tkinter import Frame, Button
from tkinter import NSEW
from Interfaces import ViewInterface


class View(ViewInterface.ViewInterface):
    """View class for the Clicker component"""

    optionsFrame = oneVsOneBtn = monkeyBtn = aiBtn = restartBtn = None

    def __init__(self, Controller):
        self.controller = Controller

    def setupGui(self, MasterFrame):
        # add options frame
        self.optionsFrame = Frame(MasterFrame, width=1, height=1)
        self.optionsFrame.grid(row=0, column=0, sticky=NSEW)
        # configure weight and amount of columns and rows
        self.configureEvenWeight(self.optionsFrame, 6, 3)
        # add 1v1 button
        self.oneVsOneBtn = Button(self.optionsFrame, command=lambda: self.onevOne_onClick(), text='1 v 1', relief='sunken', borderwidth=2, width=10, height=5)
        self.oneVsOneBtn.grid(row=1, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add monkey buttons
        self.monkeyBtn = Button(self.optionsFrame, command=lambda: self.onevsMonkey_onClick(), text='You vs. Monkey', relief='sunken', borderwidth=2, width=10, height=5)
        self.monkeyBtn.grid(row=2, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add ai buttons
        self.aiBtn = Button(self.optionsFrame, command=lambda: self.onevAi_onClick(), text='You vs. ai', relief='sunken', borderwidth=2, width=10, height=5)
        self.aiBtn.grid(row=3, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)
        # add restart button
        self.restartBtn = Button(self.optionsFrame, command=lambda: self.restart_onClick(), text='Restart', relief='sunken', borderwidth=2, width=10, height=5)
        self.restartBtn.grid(row=4, column=2, padx=(10, 50), pady=(10, 10), sticky=NSEW)

    def onevOne_onClick(self):
        # change mode, ask if wanted
        self.controller.changeMode(1)

    def onevsMonkey_onClick(self):
        # change mode, ask if wanted
        self.controller.changeMode(2)

    def onevAi_onClick(self):
        # change mode, ask if wanted
        self.controller.changeMode(3)

    def restart_onClick(self):
        # reset the game
        self.controller.resetGame()
