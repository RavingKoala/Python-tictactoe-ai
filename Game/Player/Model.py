### todo: CLASS
# 1 TODO: add comments


class Model():
    """Model class for the Player component"""

    playerName = None

    def setPlayerName(self, PlayerName):
        self.playerName = PlayerName

    def getPlayerName(self):
        return self.playerName

    playerIcon = None

    def setPlayerIcon(self, PlayerIcon):
        self.playerIcon = PlayerIcon

    def getPlayerIcon(self):
        return self.playerIcon

    assignedLabel = None

    def setAssignedLabel(self, AssignedLabel):
        self.assignedLabel = AssignedLabel

    def getAssignedLabel(self):
        return self.assignedLabel
