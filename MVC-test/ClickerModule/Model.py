import View
import Controller


class ClickerModel():
    """Model class for the Clicker Component"""

    view = controller = None

    def __init__(self):
        self.setupComponents()

    def setupComponents(self):
        self.view = View.ClickerView()
        self.controller = Controller.ClickerController()

    def setupGui(self, MainFrame):
        self.view.setupGui(MainFrame)

    def resetClicker(self):
        self.view.button1_setText(0)

    def changeButtonValue(self):
        oldInt = self.view.button1_getText()
        self.view.button1_setText(oldInt+1)
