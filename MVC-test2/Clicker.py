from tkinter import Button, NSEW


class Main():
    """main class of Cliker"""

    View = controller = model = None

    def __init__(self, MasterFrame):
        self.setupComponents()
        self.view.setupGui(MasterFrame)
        self.resetGame()

    def setupComponents(self):
        self.view = View()
        self.controller = Controller()
        self.model = Model()

        self.view.addClasses(self.controller)
        self.controller.addClasses(self.model)
        self.model.addClasses(self.view, self.controller)

    def resetGame(self):
        self.model.resetClicker()
        self.model.incrementInt = 1


class View():
    """View class for the Clicker Component"""

    controller = button = button1 = None

    def __init__(self):
        pass

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
    """Controller class for the Clicker Component"""

    model = None

    def __init__(self):
        pass

    def addClasses(self, ModelClass):
        self.model = ModelClass

    def clicked(self):
        self.model.changeButtonValue()


class Model():
    """Model class for the Clicker Component"""

    view = controller = None
    incrementInt = 1

    def __init__(self):
        pass

    def addClasses(self, ViewClass, ControllerClass):
        self.view = ViewClass
        self.controller = ControllerClass

    def setupGui(self, MainFrame):
        self.view.setupGui(MainFrame)

    def resetClicker(self):
        self.view.button1_setText(0)

    def changeButtonValue(self):
        oldInt = self.view.button1_getText()
        self.view.button1_setText(oldInt + self.incrementInt)
