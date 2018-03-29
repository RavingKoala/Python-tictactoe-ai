from tkinter import Button, NSEW
import Controller


class ClickerView():
    """View class for the Clicker Component"""

    controller = button = button1 = None

    def __init__(self):
        self.setupComponents()

    def setupComponents(self):
        self.controller = Controller.ClickerController()

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
