### todo: CLASS
# 1 TODO:


class ViewInterface():
    """Interface for Viewclasses"""

    @staticmethod
    def configureEvenWeight(Component, Y, X):
        for I in range(Y):
            Component.grid_rowconfigure(I, weight=1)
        for I in range(X):
            Component.grid_columnconfigure(I, weight=1)
