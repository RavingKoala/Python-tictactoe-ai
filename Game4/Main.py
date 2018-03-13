### todo: GENERAL
# 1 TODO: add consistent, frequent comments
# 2 TODO: use HeadClass' functions and add as many functions as wanted
# 3 TODO: Finish Gamemaster and add more functionality

# todo -> CLASS
# 1 TODO: add keybinds

from tkinter import Tk
from HeadClasses import Component
import Turn
import TicTacToe
import Options


class Main(Component.HeadComponent):
    ''' main class
        start of the application
    '''

    fullscreen = None
    popupsEnabled = True

    def __init__(self):
        # running init from parent class
        super(Main, self).__init__()
        self.masterFrame = self.root = Tk()
        # set percentage of stretch
        self.configureEvenWeight(self.masterFrame, 1, 3)
        self.masterFrame.minsize(500, 400)

    def start(self):
        self.setupComponents()
        self.root.title("tic tac toe")
        self.setkeybinds()
        self.root.attributes("-alpha", 1)
        # self.root.attributes("-fullscreen", True)
        # self.fullscreen = True
        self.root.mainloop()

    def setkeybinds(self):
        self.root.bind('<Escape>', self.escapeFullscreen)
        self.root.bind('<F11>', self.toggleFullscreen)

    def toggleFullscreen(self, _event):
        self.fullscreen = not self.fullscreen  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.fullscreen)

    def escapeFullscreen(self, _event):
        #_event -> _ = unused
        self.root.attributes("-fullscreen", False)
        self.fullscreen = False

    def setupComponents(self):
        # declare classes
        options = Options.MainOptions(self.popupsEnabled)
        ticTacToe = TicTacToe.MainTicTacToe(self.popupsEnabled)
        turn = Turn.MainTurn()
        # connect classes
        options.addClasses(turn, ticTacToe)
        ticTacToe.addClasses(turn)
        turn.addClasses(ticTacToe)
        # setup gui
        options.addGui(self.masterFrame)
        ticTacToe.addGui(self.masterFrame)
        turn.addGui(self.masterFrame)


# start app only if directly accessed
if __name__ == "__main__":
    app = Main()
    app.start()
