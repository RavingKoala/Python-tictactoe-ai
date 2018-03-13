import tkinter as TK


class MainTurnTracker():
    player = 'X'

    def addGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnTrackerFrame = TK.Frame(MasterFrame, width=1, height=1)
        self.turnTrackerFrame.grid(row=0, column=2, sticky='nes')
        # adds current turn buttons
        self.XLbl = TK.Label(self.turnTrackerFrame, text='Player1', background='green2', width=10, height=5)
        self.XLbl.grid(row=0, column=0, padx=(50, 10), pady=(10, 10), sticky='nes')
        self.OLbl = TK.Label(self.turnTrackerFrame, text='Player2', background='white', width=10, height=5)
        self.OLbl.grid(row=1, column=0, padx=(50, 10), pady=(10, 10), sticky='nes')

    def ToggleColor(self):
        if self.player == 'X':
            self.OLbl.configure(background='white')
            self.XLbl.configure(background='green2')
            self.player = 'O'
        elif self.player == 'O':
            self.XLbl.configure(background='white')
            self.OLbl.configure(background='green2')
            self.player = 'X'

    def getCurTurn(self):
        return self.player

    def setMode(self, Mode):
        if Mode == 1:
            self.XLbl.configure(text='Player1')
            self.OLbl.configure(text='Player2')
        elif Mode == 2:
            self.XLbl.configure(text='Player')
            self.OLbl.configure(text='AI')
