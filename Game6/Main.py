### todo: GENERAL
# 1 TODO: add consistent, frequent comments
# 2 TODO: use HeadClass' functions and add as many functions as wanted
# 3 TODO: Finish Gamemaster and add more functionality

### todo: CLASS
# 1 TODO: add comments

from tkinter import Tk
from HeadClasses import Component
import Options
import TicTacToe
import Turn
import Monkey
import Ai


class Main(Component.HeadComponent):
    ''' main class
        start of the application
    '''

    Options = TicTacToe = Turn = Monkey = Ai = None

    fullscreen = True
    popupsEnabled = True

    testText = 1

    def __init__(self):
        self.masterFrame = self.root = Tk()
        # set percentage of stretch
        self.configureEvenWeight(self.masterFrame, 1, 3)
        self.masterFrame.minsize(500, 400)
        if self.fullscreen:
            self.activateFullscreen()

    def start(self):
        self.setupComponents()
        self.root.title("tic tac toe")
        self.root.iconbitmap('Images/favicon.ico')
        self.setKeybinds()
        self.root.mainloop()

    def setKeybinds(self):
        self.root.bind('<Escape>', self.escapeFullscreen)
        self.root.bind('<Delete>', self.escapeFullscreen)
        self.root.bind('<Control-f>', self.toggleFullscreen)
        self.root.bind('<F11>', self.toggleFullscreen)
        self.root.bind('<Control-r>', self.resetGame)
        self.root.bind('<Control-w>', self.quit)
        self.root.bind('<Control-Key-1>', self.setMode1)
        self.root.bind('<Control-Key-2>', self.setMode2)
        self.root.bind('<Control-Key-3>', self.setMode3)
        self.root.bind('<Control-Key-4>', self.setMode4)
        self.root.bind('<Control-Key-5>', self.setMode5)

    def quit(self, _event=None):  # _var = unused
        self.root.destroy()

    def setMode1(self, _event=None):
        self.TicTacToe.ChangeMode(1)

    def setMode2(self, _event=None):
        self.TicTacToe.ChangeMode(2)

    def setMode3(self, _event=None):
        self.TicTacToe.ChangeMode(3)

    def setMode4(self, _event=None):
        self.TicTacToe.ChangeMode(4)

    def setMode5(self, _event=None):
        self.TicTacToe.ChangeMode(5)

    def resetGame(self, _event=None):
        self.TicTacToe.resetGame()

    def activateFullscreen(self):
        self.root.attributes("-fullscreen", True)
        self.fullscreen = True

    def toggleFullscreen(self, _event=None):
        self.fullscreen = not self.fullscreen  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.fullscreen)

    def escapeFullscreen(self, _event=None):
        self.root.attributes("-fullscreen", False)
        self.fullscreen = False

    def setupComponents(self):
        # declare classes
        self.Options = Options.MainOptions(self.popupsEnabled)
        self.TicTacToe = TicTacToe.MainTicTacToe(self.popupsEnabled)
        self.Turn = Turn.MainTurn()
        self.Ai = Ai.MainAi()
        self.Monkey = Monkey.MainMonkey()
        # connect classes
        self.Options.addClasses(self.TicTacToe)
        self.TicTacToe.addClasses(self.Turn)
        self.Turn.addClasses(self.TicTacToe, self.Monkey, self.Ai)
        self.Ai.addClasses(self.TicTacToe)
        self.Monkey.addClasses(self.TicTacToe)
        # setup gui
        self.Options.addGui(self.masterFrame)
        self.TicTacToe.addGui(self.masterFrame)
        self.Turn.addGui(self.masterFrame)

        self.TicTacToe.ChangeMode(1)


# start app only if directly accessed
if __name__ == "__main__":
    app = Main()
    app.start()
