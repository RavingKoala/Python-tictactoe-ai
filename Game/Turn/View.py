from tkinter import Frame, Label
from tkinter import NSEW
from Interfaces import ViewInterface


class View(ViewInterface.ViewInterface):

    turnFrame = label1 = label2 = None

    def __init__(self, Controller):
        self.controller = Controller

    def setupGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnFrame = Frame(MasterFrame, width=1, height=1)
        self.turnFrame.grid(row=0, column=2, sticky=NSEW)
        # configure weight and amount of columns and rows
        self.configureEvenWeight(self.turnFrame, 6, 3)
        # adds current turn buttons
        self.label1 = Label(self.turnFrame, width=10, height=5)
        self.label1.grid(row=2, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)
        self.label2 = Label(self.turnFrame, width=10, height=5)
        self.label2.grid(row=3, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)

    def changeBackgroundColor(self, LabelOneBGC=None, LabelTwoBGC=None):
        if LabelOneBGC != None:
            self.label1.configure(background=LabelOneBGC)
        if LabelTwoBGC != None:
            self.label2.configure(background=LabelTwoBGC)

    def updateLabelText(self, LabelOneText=None, LabelTwoText=None):
        if LabelOneText != None:
            self.label1.configure(text=LabelOneText)
        if LabelTwoText != None:
            self.label2.configure(text=LabelTwoText)
