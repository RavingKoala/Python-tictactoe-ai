### todo: CLASS
# 1 TODO: add comments

from tkinter import Frame, Button
from tkinter import NSEW
from Interfaces import ViewInterface


class View(ViewInterface.ViewInterface):
    """View class for the TicTacToe component"""

    TTTButtons = []
    controller = dimensions = TTTFrame = None

    def __init__(self, Controller):
        self.controller = Controller

    def setSettings(self, dimensionDict):
        self.dimensions = dimensionDict

    def setupGui(self, MasterFrame):
        # add TicTacToe frame
        self.TTTFrame = Frame(MasterFrame)
        self.TTTFrame.grid(row=0, column=1, sticky=NSEW)
        self.configureEvenWeight(self.TTTFrame, self.dimensions, self.dimensions)

        # add the buttons
        for y in range(self.dimensions):
            self.TTTButtons.append([])
            for x in range(self.dimensions):
                self.TTTButtons[y].append(Button(self.TTTFrame, command=lambda Y=y, X=x: self.TTTBtn_onClick(Y, X), font='calibri 34 bold', text="", relief='groove', borderwidth=3, width=3, height=1))
                self.TTTButtons[y][x].grid(row=y, column=x, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky=NSEW)

    def TTTBtn_onClick(self, Y, X):
        self.controller.buttonClicked(Y, X)

    def setBtnText(self, Y, X, Text):
        self.TTTButtons[Y][X].configure(text=Text)

    def disableButton(self, Y, X):
        self.TTTButtons[Y][X].configure(state='disabled')

    def enableButton(self, Y, X):
        self.TTTButtons[Y][X].configure(state='normal')
