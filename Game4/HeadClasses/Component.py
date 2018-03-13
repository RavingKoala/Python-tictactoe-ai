# 1 TODO:

# pylint: disable=too-few-public-methods


class HeadComponent():
    '''default functionality for component classes'''

    masterFrame = testFrame = testLabel = None

    def __init__(self):
        pass

    @staticmethod
    def configureEvenWeight(Component, Y, X):
        for I in range(Y):
            Component.grid_rowconfigure(I, weight=1)
        for I in range(X):
            Component.grid_columnconfigure(I, weight=1)
