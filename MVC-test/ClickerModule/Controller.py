import Model


class ClickerController():
    """Controller class for the Clicker Component"""

    model = None

    def __init__(self):
        self.setupComponents()

    def setupComponents(self):
        self.model = Model.ClickerModel()

    def clicked(self):
        self.model.changeButtonValue()
