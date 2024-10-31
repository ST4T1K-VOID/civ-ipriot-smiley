import time

import smiley
from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
       Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [9, 14, 18, 21 ]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()