from tkinter import Button, NSEW


class Main():
    """main class of the Clicker component"""

    View = controller = model = None

    def __init__(self, MasterFrame):
        self.setupComponents()
        self.view.setupGui(MasterFrame)
        self.setKeybinds(MasterFrame)
        self.resetGame()

    def setKeybinds(self, Root):
        Root.bind('<Control-r>', self.resetGame)

    def setupComponents(self):
        self.view = View()
        self.controller = Controller()
        self.model = Model()

        self.view.addClasses(self.controller)
        self.controller.addClasses(self.view, self.model)
        # self.model.addClasses()

    def resetGame(self):
        self.controller.resetClicker()
        self.model.incrementInt = 1


class View():
    """View class for the Clicker component"""

    controller = button = button1 = None

    # def __init__(self):
    #     pass

    def addClasses(self, ControllerClass):
        self.controller = ControllerClass

    def setupGui(self, MainFrame):
        self.button1 = Button(MainFrame, command=lambda: self.button1_onClick(), relief='sunken', borderwidth=2, width=10, height=5)
        self.button1.grid(row=1, column=1, padx=(0, 0), pady=(0, 0), sticky=NSEW)

    def button1_onClick(self):
        self.controller.clicked()

    def button1_setText(self, Text):
        self.button1.configure(text=Text)

    def button1_getText(self):
        return self.button1['text']

    def button1_disable(self):
        self.button1.configure(state="disabled")

    def button1_enable(self):
        self.button1.configure(state="normal")


class Controller():
    """Controller class for the Clicker component"""

    view = model = None

    def __init__(self):
        pass

    def addClasses(self, ViewClass, ModelClass):
        self.view = ViewClass
        self.model = ModelClass

    def clicked(self):
        self.model.updateButtonValue()
        newButtonValue = self.model.getButtonValue()
        self.view.button1_setText(newButtonValue)

    def resetClicker(self):
        self.model.resetButtonValue()
        newButtonValue = self.model.getButtonValue()
        self.view.button1_setText(newButtonValue)


class Model():
    """Model class for the Clicker component"""

    view = controller = None
    buttonValue = 0
    incrementInt = 0

    def getButtonValue(self):
        return self.buttonValue

    def updateButtonValue(self):
        self.buttonValue += self.incrementInt

    def resetButtonValue(self):
        self.buttonValue = 0

    def resetIncrementIntValue(self):
        self.incrementInt = 1
