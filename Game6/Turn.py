### todo: CLASS
# 1 TODO: create object containing playeble and name

from tkinter import Frame, Label
from tkinter import NSEW
from HeadClasses import Component


class MainTurn(Component.HeadComponent):
    ''' Turn class
        contains data that shows who's turn it is
    '''

    # predeclaring attributes
    players = [{"playerName": "Player1", "isPlaying": True, "isMyTurn": True, "PlayerIcon": "X", "label": "label1"},
               {"playerName": "Player2", "isPlaying": True, "isMyTurn": False, "PlayerIcon": "O", "label": "label2"},
               {"playerName": "AI", "isPlaying": False, "isMyTurn": False, "PlayerIcon": "", "label": ""},
               {"playerName": "AI2", "isPlaying": False, "isMyTurn": False, "PlayerIcon": "", "label": ""}]
    turnFrame = Label1 = Label2 = TTTGame = None

    def addClasses(self, TicTacToe):
        self.TTTGame = TicTacToe

    def addGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnFrame = Frame(MasterFrame, width=1, height=1)
        self.turnFrame.grid(row=0, column=2, sticky=NSEW)
        self.configureEvenWeight(self.turnFrame, 6, 3)
        # adds current turn buttons
        self.Label1 = Label(self.turnFrame, text=self.players[0]['playerName'], background='green2', width=10, height=5)
        self.Label1.grid(row=2, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)
        self.Label2 = Label(self.turnFrame, text=self.players[1]['playerName'], background='white', width=10, height=5)
        self.Label2.grid(row=3, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)

    def toggleColor(self):
        if self.player == 'X':
            self.setTurnColor('O')
        elif self.player == 'O':
            self.setTurnColor('X')

    def toggleTurn(self):
        self.toggleColor()

    def setTurnColor(self, Turn):
        if Turn == 'X':
            self.Label2.configure(background='white')
            self.Label1.configure(background='green2')
            self.player = 'X'
        elif Turn == 'O':
            self.Label1.configure(background='white')
            self.Label2.configure(background='green2')
            self.player = 'O'

    def getPlaying(self):
        playing = []
        for player in self.players:
            if player['isplaying']:
                playing.append(player)
        return playing

    def resetTurn(self):
        self.setTurnColor('X')

    def setTurn(self, Player=None, PlayerName=None, PlayerIcon=None):
        if Player != None:
            self.players[Player]['isMyTurn'] = True
        elif PlayerName != None:
            self.players[Player]['isMyTurn'] = True
        elif PlayerIcon != None:
            pass

    def getTurn(self):
        for player in self.players:
            if player['isMyTurn']:
                return player
        return "unknown"
