import tkinter as TK
from math import floor
# import TurnTracker


class MainTicTacToe():
    # create TTTButtons list containing the Game buttons
    TTTButtons = []

    def __init__(self, TurnTracker):
        self.TurnTracker = TurnTracker

    def addGui(self, MasterFrame):
        # add TicTacToe frame
        self.tttFrame = TK.Frame(MasterFrame)
        self.tttFrame.grid(row=0, column=1, sticky='nesw')

        # add the buttons
        for I in range(0, 9):
            self.TTTButtons.append(TK.Button(self.tttFrame, command=lambda nr=I: self.onClick(nr), background='white', font='calibri 34 bold', text='', width=3, height=1))
            rowI = floor(I / 3)
            columnI = floor(I % 3)
            self.TTTButtons[I].grid(row=rowI, column=columnI, ipadx=(0), ipady=(0), padx=(5, 5), pady=(5, 5), sticky='nesw')

    def setBtnText(self, I, Text):
        self.TTTButtons[I].configure(text=Text)

    def onClick(self, I):
        text = self.TurnTracker.getCurTurn()
        self.setBtnText(I, text)
        self.TurnTracker.ToggleColor()
