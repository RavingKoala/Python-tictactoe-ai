# this test application will have an input field and an button.
# Once you click the button the text inside the input field will be put on the button

# 1. TODO: create mainFrame
# 2. TODO:

from tkinter import Tk
from ClickerModule import Model as Clicker


class Main():
    '''Main class for testing a MVC-structure'''

    clicker = None

    def __init__(self):
        self.mainFrame = self.root = Tk()
        self.mainFrame.grid_columnconfigure(3, weight=1)
        self.mainFrame.grid_rowconfigure(3, weight=1)
        self.mainFrame.minsize(200, 100)

    def start(self):
        self.setupComponents()
        self.root.mainloop()

    def setupComponents(self):
        self.clicker = Clicker.ClickerModel()

        self.clicker.resetClicker()

        # start app only if directly accessed
if __name__ == "__main__":
    app = Main()
    app.start()
