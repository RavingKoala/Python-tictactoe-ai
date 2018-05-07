from . import View
from . import Model
from Interfaces import ControllerInterface
from random import randint


class Controller(ControllerInterface.ControllerInterface):
    """Controller class for the Turn component"""

    ticTacToe = monkey = ai = None

    def __init__(self):
        self.view = View.View(self)
        self.model = Model.Model()

    def addClasses(self, TicTacToe, Player):
        self.ticTacToe = TicTacToe
        self.player = Player

    def initialize(self, MasterFrame):
        self.view.setupGui(MasterFrame)

    def getPlayerIcon(self):
        return self.model.playingPlayers[self.model.getTurn()]['playerIcon']

    def changeTurn(self):
        newTurn = (self.model.getTurn() + 1) % 2
        self.setTurn(newTurn)
        self.updateTurnColor()

    def updateTurnColor(self):
        LabelNr = self.model.playingPlayers[self.model.getTurn()]['label']

        if LabelNr == 'label1':
            self.view.changeBackgroundColor('green2', 'white')
        elif LabelNr == 'label2':
            self.view.changeBackgroundColor('white', 'green2')

    def updateLabelText(self):
        self.view.updateLabelText(LabelOneText=self.model.playingPlayers[0]['playerName'] + "\n" + self.model.playingPlayers[0]['playerIcon'])
        self.view.updateLabelText(LabelTwoText=self.model.playingPlayers[1]['playerName'] + "\n" + self.model.playingPlayers[1]['playerIcon'])

    def resetTurn(self):
        self.setTurn(randint(0, 1))
        self.updateTurnColor()

    def setTurn(self, PlayerNr):
        self.model.setTurn(PlayerNr)
        turnName = self.getPlayerName()
        if turnName == "player1" or turnName == "player2":
            self.ticTacToe.enableButtons()
        else:
            self.ticTacToe.disableButtons()
            # if turnName == "monkey" or turnName == "monkey2":
            #     self.monkey.requestMove()
            # if turnName == "ai" or turnName == "ai2":
            #     self.ai.requestMove()

    def getPlayerName(self):
        return self.model.playingPlayers[self.model.getTurn()]['playerName']

    def setMode(self, Mode):
        self.clearPlayerData()
        self.appointPlayers(Mode)
        self.updatePlayerData()
        self.updateLabelText()
        self.resetTurn()

    def clearPlayerData(self):
        for player in self.model.playingPlayers:
            player['playerIcon'] = ""
            player['label'] = ""

    def appointPlayers(self, Mode):
        self.model.playingPlayers = []
        if Mode == 1:
            self.model.playingPlayers.append(self.model.players[0])
            self.model.playingPlayers.append(self.model.players[1])
        elif Mode == 2:
            self.model.playingPlayers.append(self.model.players[0])
            self.model.playingPlayers.append(self.model.players[2])
        elif Mode == 3:
            self.model.playingPlayers.append(self.model.players[0])
            self.model.playingPlayers.append(self.model.players[4])
        elif Mode == 4:
            self.model.playingPlayers.append(self.model.players[2])
            self.model.playingPlayers.append(self.model.players[3])
        elif Mode == 5:
            self.model.playingPlayers.append(self.model.players[4])
            self.model.playingPlayers.append(self.model.players[5])

    def updatePlayerData(self):
        self.setPlayerLabel()
        self.setRandomplayerIcon()

    def setPlayerLabel(self):
        self.model.playingPlayers[0]['label'] = "label1"
        self.model.playingPlayers[1]['label'] = "label2"

    def setRandomplayerIcon(self):
        playerIndex = randint(0, 1)
        self.model.playingPlayers[playerIndex]['playerIcon'] = "X"
        self.model.playingPlayers[1 if playerIndex == 0 else 0]['playerIcon'] = "O"
