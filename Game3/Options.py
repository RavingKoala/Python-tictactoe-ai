import tkinter as TK
# import TurnTracker
# import TicTacToe


class MainOptions():
    def __init__(self, TurnTracker, TicTacToe):
        self.TTTGame = TicTacToe
        self.TurnTracker = TurnTracker

    def addGui(self, MasterFrame):
        # add options frame
        self.optionsFrame = TK.Frame(MasterFrame, width=1, height=1)
        self.optionsFrame.grid(row=0, column=0, sticky='nsw')
        # add 1v1 button
        self.oneVsOneBtn = TK.Button(self.optionsFrame, command=lambda: self.OnevOne_onClick(), background='white', text='1 v 1', width=10, height=5)
        self.oneVsOneBtn.grid(row=0, column=0, padx=(10, 50), pady=(10, 10), sticky='nsw')
        # add ai button
        self.aiBtn = TK.Button(self.optionsFrame, command=lambda: self.OnevAi_onClick(), background='white', text='Play vs. AI', width=10, height=5)
        self.aiBtn.grid(row=1, column=0, padx=(10, 50), pady=(10, 10), sticky='nsw')
        # add restart button
        self.restartBtn = TK.Button(self.optionsFrame, command=lambda: self.Restart_onClick(), background='white', text='Restart', width=10, height=5)
        self.restartBtn.grid(row=2, column=0, padx=(10, 50), pady=(10, 10), sticky='nsw')

    def OnevOne_onClick(self):
        self.TurnTracker.setMode(1)

    def OnevAi_onClick(self):
        self.TurnTracker.setMode(2)

    def Restart_onClick(self):
        for I in range(0, 9):
            self.TTTGame.setBtnText(I, "")
