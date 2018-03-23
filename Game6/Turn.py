### todo: CLASS
# 1 TODO: add comments

from tkinter import Frame, Label
from tkinter import NSEW
from random import randint
from HeadClasses import Component


class MainTurn(Component.HeadComponent):
    ''' Turn class
        contains data that shows who's turn it is
    '''

    # predeclaring attributes
    turnFrame = label1 = label2 = TTTGame = ai = monkey = None

    players = [{'playerName': "player1", 'playerIcon': "", 'label': ""},
               {'playerName': "player2", 'playerIcon': "", 'label': ""},
               {'playerName': "monkey", 'playerIcon': "", 'label': ""},
               {'playerName': "monkey2", 'playerIcon': "", 'label': ""},
               {'playerName': "AI", 'playerIcon': "", 'label': ""},
               {'playerName': "AI2", 'playerIcon': "", 'label': ""}]

    playingPlayers = [players[0], players[1]]

    turn = 0

    def addClasses(self, TicTacToeClass, MonkeyClass, AiClass):
        self.TTTGame = TicTacToeClass
        self.monkey = MonkeyClass
        self.ai = AiClass

    def addGui(self, MasterFrame):
        # create new frame for tracking who's turn it is
        self.turnFrame = Frame(MasterFrame, width=1, height=1)
        self.turnFrame.grid(row=0, column=2, sticky=NSEW)
        self.configureEvenWeight(self.turnFrame, 6, 3)
        # adds current turn buttons
        self.label1 = Label(self.turnFrame, width=10, height=5)
        self.label1.grid(row=2, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)
        self.label2 = Label(self.turnFrame, width=10, height=5)
        self.label2.grid(row=3, column=0, padx=(50, 10), pady=(10, 10), sticky=NSEW)

    def getPlayerIcon(self):
        return self.playingPlayers[self.getTurn()]['playerIcon']

    def changeTurn(self):
        newTurn = (self.getTurn() + 1) % 2
        self.setTurn(newTurn)
        self.updateTurnColor()

    def updateTurnColor(self):
        LabelNr = self.playingPlayers[self.getTurn()]['label']

        if LabelNr == 'label1':
            self.label1.configure(background='green2')
            self.label2.configure(background='white')
        elif LabelNr == 'label2':
            self.label1.configure(background='white')
            self.label2.configure(background='green2')

    def updateLabelText(self):
        self.label1.configure(text=self.playingPlayers[0]['playerName'] + "\n" + self.playingPlayers[0]['playerIcon'])
        self.label2.configure(text=self.playingPlayers[1]['playerName'] + "\n" + self.playingPlayers[1]['playerIcon'])

    def resetTurn(self):
        self.setTurn(randint(0, 1))
        self.updateTurnColor()

    def setTurn(self, Int):
        self.turn = Int
        turnName = self.getPlayerName()
        if turnName == "player1" or turnName == "player2":
            self.TTTGame.enableButtons()
        else:
            self.TTTGame.disableButtons()
            if turnName == "monkey" or turnName == "monkey2":
                self.monkey.requestMove()
            if turnName == "AI" or turnName == "AI2":
                self.ai.requestMove()

    def getTurn(self):
        return self.turn

    def getPlayerName(self):
        return self.playingPlayers[self.getTurn()]['playerName']

    def setMode(self, Mode):
        self.clearPlayerData()
        self.appointPlayers(Mode)
        self.updatePlayerData()
        self.updateLabelText()
        self.resetTurn()

    def clearPlayerData(self):
        for player in self.playingPlayers:
            player['playerIcon'] = ""
            player['label'] = ""

    def appointPlayers(self, Mode):
        self.playingPlayers = []
        if Mode == 1:
            self.playingPlayers.append(self.players[0])
            self.playingPlayers.append(self.players[1])
        elif Mode == 2:
            self.playingPlayers.append(self.players[0])
            self.playingPlayers.append(self.players[2])
        elif Mode == 3:
            self.playingPlayers.append(self.players[0])
            self.playingPlayers.append(self.players[4])
        elif Mode == 4:
            self.playingPlayers.append(self.players[2])
            self.playingPlayers.append(self.players[3])
        elif Mode == 5:
            self.playingPlayers.append(self.players[4])
            self.playingPlayers.append(self.players[5])

    def updatePlayerData(self):
        self.setPlayerLabel()
        self.setRandomplayerIcon()

    def setPlayerLabel(self):
        self.playingPlayers[0]['label'] = "label1"
        self.playingPlayers[1]['label'] = "label2"

    def setRandomplayerIcon(self):
        playerIndex = randint(0, 1)
        self.playingPlayers[playerIndex]['playerIcon'] = "X"
        self.playingPlayers[1 if playerIndex == 0 else 0]['playerIcon'] = "O"
