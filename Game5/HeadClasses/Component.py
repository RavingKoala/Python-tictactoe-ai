### todo: CLASS
# 1 TODO: add keybinds
# 2 TODO: set tooltip option, with keybinds info for buttons

# pylint: disable=too-few-public-methods


class HeadComponent():
    '''default functionality for component classes'''

    masterFrame = testFrame = testLabel = None

    @staticmethod
    def configureEvenWeight(Component, Y, X):
        for I in range(Y):
            Component.grid_rowconfigure(I, weight=1)
        for I in range(X):
            Component.grid_columnconfigure(I, weight=1)
