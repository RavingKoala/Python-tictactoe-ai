# todo: CLASS
# 1 TODO: add comments


class Model():
    """Model class for the TicTacToe component"""

    popupsEnabled = None

    TTTButtonsText = [["", "", ""], ["", "", ""], ["", "", ""]]

    dimensions = 3

    mode = 0

    buttonsEnabled = False

    def setSettings(self, PopupsEnabled, dimensionDict):
        self.setPopupsEnabled(PopupsEnabled)
        self.setDimensions(dimensionDict)

    def setPopupsEnabled(self, Bool):
        self.popupsEnabled = Bool

    def getPopupsEnabled(self):
        return self.popupsEnabled

    def getDimensions(self):
        return self.dimensions

    def setDimensions(self, I):
        self.dimensions = I

    def setMode(self, Mode):
        self.mode = Mode

    def getMode(self):
        return self.mode

    def setButtonsEnabled(self, Bool):
        self.buttonsEnabled = Bool

    def getButtonsEnabled(self):
        return self.buttonsEnabled

    def setBtnText(self, Y, X, Text):
        self.TTTButtonsText[Y][X] = Text

    def getBtnText(self, Y, X):
        return self.TTTButtonsText[Y][X]

    def getAllBtnText(self):
        return [[self.TTTButtonsText[Y][X] for X in range(len(self.TTTButtonsText[Y]))] for Y in range(len(self.TTTButtonsText))]

    def getRowBtnText(self, I):
        return [buttonText for buttonText in self.TTTButtonsText[I]]

    def getColumnBtnText(self, I):
        return [buttonText[I] for buttonText in self.TTTButtonsText]
