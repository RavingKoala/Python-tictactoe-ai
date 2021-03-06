### todo: CLASS
# 1 TODO: test and verify focus of popup

from tkinter import Label, Toplevel, NSEW
from . import ViewInterface


class ControllerInterface(ViewInterface.ViewInterface):
    """Interface for Controllerclasses"""

    masterFrame = testFrame = testLabel = None

    def doPopup(self, Type="Undefined", Text="Empty"):
        toplevel = Toplevel()
        # set minimum size
        toplevel.minsize(200, 10)
        # configure weight and amount of columns and rows
        self.configureEvenWeight(toplevel, 3, 3)
        toplevel.focus_force()

        def selfDestroy(_event=None):
            toplevel.destroy()

        def setKeybinds(component):
            component.bind("<Key>", selfDestroy)

        def getPopupMessage(Type="Undefined", Text="Empty"):
            if type == "Lost":
                return "You lost." + "\n" + "Please try again!"
            elif Type == "Draw":
                return "Its a draw!" + "\n" + "Please try again!"
            elif Type == "Win":
                return "Congratulations!" + "\n" + "{0} won!".format(Text).capitalize()
            elif Type == "specialWin":
                return "Congratulations, you won against the not yet unbeatable ai." + "\n" + "That technique won't work again!".capitalize()
            return "Something went wrong." + "\n" + "Please contact the developer about this problem."

        setKeybinds(toplevel)
        label1 = Label(toplevel)
        label1.grid(row=1, column=1, sticky=NSEW)
        if Type == "Undefined" and Text == "Empty":
            message = "Something went wrong." + "\n" + "Please contact the developer about this problem."
        else:
            message = getPopupMessage(Type, Text)
        label1.configure(text=message)
