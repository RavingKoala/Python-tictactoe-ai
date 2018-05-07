# todo: GENERAL
# 1 TODO: add consistent, frequent comments5
# 2 TODO: use HeadClass' functions and add as many functions as wanted
# 3 TODO: Finish Gamemaster and add more functionality

### todo: CLASS
# 1 TODO: add comments

from tkinter import Tk
from Interfaces import ViewInterface
from Options import Controller as Options
from TicTacToe import Controller as TicTacToe
from Turn import Controller as Turn
from Player import Controller as Player


class Main(ViewInterface.ViewInterface):
    ''' main class
        start of the application
    '''

    options = ticTacToe = turn = player = None

    settings = {'fullscreen': False,
                'popupsEnabled': True,
                'dimensions': 3}

    def __init__(self):
        self.masterFrame = self.root = Tk()
        # configure weight and amount of columns and rows
        self.configureEvenWeight(self.masterFrame, 1, 3)
        # set minimum size
        self.masterFrame.minsize(500, 400)
        # if fullscreen is default start in fullscreen
        if self.settings['fullscreen']:
            self.activateFullscreen()

    def start(self):
        # apply component
        self.setupComponents()
        # change outer visuals
        self.root.title("tic tac toe")
        self.root.iconbitmap('Media/Images/favicon.ico')
        # create keyboard shortcuts
        self.setKeybinds()
        # start and show tkinter
        self.root.mainloop()

    def setupComponents(self):
        # declare classes
        self.options = Options.Controller()
        self.ticTacToe = TicTacToe.Controller()
        self.turn = Turn.Controller()
        self.player = Player.Controller()

        self.ticTacToe.setSettings(self.settings['popupsEnabled'], self.settings['dimensions'])

        self.options.initialize(self.masterFrame)
        self.ticTacToe.initialize(self.masterFrame)
        self.turn.initialize(self.masterFrame)

        # connect classes
        self.options.addClasses(self.ticTacToe)
        self.ticTacToe.addClasses(self.turn)
        self.turn.addClasses(self.ticTacToe, self.player)
        self.player.addClasses(self.ticTacToe)

        self.ticTacToe.changeMode(1)

    def setKeybinds(self):
        self.root.bind('<Control-Key-1>', self.setMode1)
        self.root.bind('<Control-Key-2>', self.setMode2)
        self.root.bind('<Control-Key-3>', self.setMode3)
        self.root.bind('<Control-Key-4>', self.setMode4)
        self.root.bind('<Control-Key-5>', self.setMode5)
        self.root.bind('<Control-r>', self.resetGame)
        self.root.bind('<Control-w>', self.quit)
        self.root.bind('<Escape>', self.escapeFullscreen)
        self.root.bind('<Delete>', self.escapeFullscreen)
        self.root.bind('<f>', self.toggleFullscreen)
        self.root.bind('<F11>', self.toggleFullscreen)

    def quit(self, _event=None):
        self.root.destroy()

    def setMode1(self, _event=None):
        self.ticTacToe.changeMode(1)

    def setMode2(self, _event=None):
        self.ticTacToe.changeMode(2)

    def setMode3(self, _event=None):
        self.ticTacToe.changeMode(3)

    def setMode4(self, _event=None):
        self.ticTacToe.changeMode(4)

    def setMode5(self, _event=None):
        self.ticTacToe.changeMode(5)

    def resetGame(self, _event=None):
        self.ticTacToe.resetGame()

    def activateFullscreen(self):
        self.root.attributes("-fullscreen", True)
        self.settings['fullscreen'] = True

    def toggleFullscreen(self, _event=None):
        self.settings['fullscreen'] = not self.settings['fullscreen']  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.settings['fullscreen'])

    def escapeFullscreen(self, _event=None):
        self.root.attributes("-fullscreen", False)
        self.settings['fullscreen'] = False


# start app only if directly accessed
if __name__ == "__main__":
    app = Main()
    app.start()
