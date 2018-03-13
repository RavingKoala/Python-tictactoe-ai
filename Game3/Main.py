import tkinter as TK


class Main():
    def __init__(self):
        self.masterFrame = self.root = TK.Tk()
        self.root.title("tic tac toe")

    def Start(self):
        self.setupComponents()
        self.root.mainloop()

    def setupComponents(self):
        import TurnTracker
        TurnTracker = TurnTracker.MainTurnTracker()
        TurnTracker.addGui(self.masterFrame)

        import TicTacToe
        TicTacToe = TicTacToe.MainTicTacToe(TurnTracker)
        TicTacToe.addGui(self.masterFrame)

        import Options
        options = Options.MainOptions(TurnTracker, TicTacToe)
        options.addGui(self.masterFrame)


if __name__ == "__main__":
    app = Main()
    app.Start()

# TODO create controller for every components
