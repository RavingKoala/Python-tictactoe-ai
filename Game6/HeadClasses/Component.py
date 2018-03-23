### todo: CLASS
# 1 TODO: add keybinds
# 2 TODO: set tooltip option, with keybinds info for buttons

from tkinter import Label, Toplevel
from tkinter import NSEW


class HeadComponent():
    '''default functionality for component classes'''

    masterFrame = testFrame = testLabel = None

    @staticmethod
    def configureEvenWeight(Component, Y, X):
        for I in range(Y):
            Component.grid_rowconfigure(I, weight=1)
        for I in range(X):
            Component.grid_columnconfigure(I, weight=1)

    @staticmethod
    def doPopup(Type="Undefined", Text="Empty"):
        toplevel = Toplevel()

        def selfDestroy():
            toplevel.destroy()

        def setKeybinds(component):
            component.bind("Any-KeyPress", selfDestroy)

        def getPopupMessage(Type="Undefined", Text="Empty"):
            if type == "Lost":
                return "you lost." + "\n" + "Please try again!"
            elif Type == "Draw":
                return "Its a draw!" + "\n" + "Please try again!"
            elif Type == "Win":
                return "Congratulations!" + "\n" + "{0} won!".format(Text).capitalize()
            elif Type == "specialWin":
                return "Congratulations, you won against the not yet unbeatable ai." + "\n" + "That technique won't work again!".capitalize()
            return "Something went wrong." + "\n" + "Please contact the developer about this problem."

        setKeybinds(toplevel)
        toplevel.minsize(100, 100)
        label1 = Label(toplevel)
        label1.grid(sticky=NSEW)
        if Type == "Undefined" and Text == "Empty":
            label1.configure(text="Something went wrong." + "\n" + "Please contact the developer about this problem.")
        else:
            message = getPopupMessage(Type, Text)
        label1.configure(text=message)
