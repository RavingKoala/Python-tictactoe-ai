import tkinter as TK
from math import floor


class Main():
    def __init__(self):
        self.root = TK.Tk()
        self.gui = Gui(self.root)
        self.gui.Main()
        self.gameMaster = GameMaster()

    def Start(self):
        self.gui.masterFrame.title("tic tac toe")
        self.root.mainloop()


class GameMaster():
    def __init__(self):
        pass

    def CheckWin(self):
        pass


class Game():
    def __init__(self, masterframe):
        self.ai = Ai()
        self.masterframe = masterframe

    def ModeBtnsHandler(self):
        pass

    def RestartBtnsHandler(self, btns):
        for btn in btns:
            btn['text'] = ""

    def TTTBtnsHandler(self, btnNr):
        pass

    def turnTrackerLblHandler(self):
        pass


class Ai():
    def __init__(self):
        pass


class Gui():
    def __init__(self, masterFrame):
        self.masterFrame = masterFrame
        self.game = Game(self.masterFrame)
        self.definevars()

    def definevars(self):
        # create optionsFrame, gameFrake, turnFrame of tic tac toe
        self.optionsFrame = self.tttFrame = self.turnTrackerFrame = None
        # create ai button, 1v1 button, restart button
        self.aiBtn = self.oneVsOneBtn = self.restartBtn = None
        # create TTTButtons list containing the game buttons
        self.TTTButtons = []
        # create XLabal and OLabal
        self.XLbl = self.OLbl = None

    def Main(self):
        self.AddFrames()
        self.AddComponents()

    def AddFrames(self):
        # add optionsFrame of tic tac toe
        self.optionsFrame = TK.Frame(self.masterFrame)
        self.optionsFrame.grid(row=0, column=0)
        # add game masterframe
        self.tttFrame = TK.Frame(self.masterFrame)
        self.tttFrame.grid(row=0, column=1)
        # create new frame for tracking who's turn it is
        self.turnTrackerFrame = TK.Frame(self.masterFrame)
        self.turnTrackerFrame.grid(row=0, column=2)

    def AddComponents(self):
        self.AddModeButtons()
        self.AddRestartButton()
        self.AddTTT()
        self.AddTurnTracker()

    def AddModeButtons(self):
        # add ai button
        self.aiBtn = TK.Button(self.optionsFrame, command=self.game.ModeBtnsHandler(), text='Play vs. AI', width=10, height=5)
        self.aiBtn.grid(row=0, column=0, padx=(10, 50), pady=(10, 10))
        # add 1v1 button
        self.oneVsOneBtn = TK.Button(self.optionsFrame, text='1 v 1', command=self.game.ModeBtnsHandler(), width=10, height=5)
        self.oneVsOneBtn.grid(row=1, column=0, padx=(10, 50), pady=(10, 10))

    def AddRestartButton(self):
        # add restart button
        self.restartBtn = TK.Button(self.optionsFrame, text='Restart', command=self.game.RestartBtnsHandler(self.TTTButtons), width=10, height=5)
        self.restartBtn.grid(row=2, column=0, padx=(10, 50), pady=(10, 10))

    def AddTTT(self):
        # add the buttons
        for I in range(0, 9):
            self.TTTButtons.append(TK.Button(self.tttFrame, command=self.game.TTTBtnsHandler(I), width=10, height=5))
            rowI = floor(I / 3)
            columnI = floor(I % 3)
            self.TTTButtons[I].grid(row=rowI, column=columnI, padx=(10, 10), pady=(10, 10))

    def AddTurnTracker(self):
        # adds current turn buttons
        self.XLbl = TK.Label(self.turnTrackerFrame, text='X', command=self.game.turnTrackerLblHandler(), width=10, height=5)
        self.XLbl.grid(row=0, column=0, padx=(50, 10), pady=(10, 10))
        self.OLbl = TK.Label(self.turnTrackerFrame, text='O', command=self.game.turnTrackerLblHandler(), width=10, height=5)
        self.OLbl.grid(row=1, column=0, padx=(50, 10), pady=(10, 10))


if __name__ == "__main__":
    app = Main()
    app.Start()
