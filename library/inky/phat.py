"""Inky pHAT e-Ink Display Driver."""
from . import inky, inky2


class InkyPHAT2(inky2.Inky):
    """Inky pHAT V2 (250x122 pixel) e-Ink Display Driver."""

    WIDTH = 250
    HEIGHT = 122

    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour):
        """Initialise an Inky pHAT Display.

        :param colour: one of red, black or yellow, default: black

        """
        inky2.Inky.__init__(
            self,
            resolution=(self.WIDTH, self.HEIGHT),
            colour=colour,
            h_flip=False,
            v_flip=False)


class InkyPHAT(inky.Inky):
    """Inky wHAT e-Ink Display Driver."""

    WIDTH = 212
    HEIGHT = 104

    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour):
        """Initialise an Inky pHAT Display.

        :param colour: one of red, black or yellow, default: black

        """
        inky.Inky.__init__(
            self,
            resolution=(self.WIDTH, self.HEIGHT),
            colour=colour,
            h_flip=False,
            v_flip=False)
