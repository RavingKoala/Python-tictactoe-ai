### todo: CLASS
# 1 TODO: add comments


class Model():
    """Model class for the TicTacToe component"""

    # players = [{'playerName': "player1", 'playerIcon': "", 'label': ""},
#            {'playerName': "player2", 'playerIcon': "", 'label': ""},
#            {'playerName': "monkey", 'playerIcon': "", 'label': ""},
#            {'playerName': "monkey2", 'playerIcon': "", 'label': ""},
#            {'playerName': "ai", 'playerIcon': "", 'label': ""},
#            {'playerName': "ai2", 'playerIcon': "", 'label': ""}]
#
# def getplayer(self, I=None, PlayerName=None):
#     if I != None:
#         return self.players[I]
#     elif PlayerName != None:
#         for player in self.players:
#             if player['playerName'] == PlayerName:
#                 return player
#     return None
#
    playingPlayers = []

    def getplayingPlayers(self):
        return self.playingPlayers

    def setPlayingPlayers(self, Player1, Player2):
        self.playingPlayers.append(Player1)
        self.playingPlayers.append(Player2)

    turn = 0

    def setTurn(self, Turn):
        self.turn = Turn

    def getTurn(self):
        return self.turn
