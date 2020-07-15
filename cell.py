# Conway's Game of Life - Python Implementation
# Author: Daniel: dan@imdany.com

import pygame
from config import *

# Logic of the Cell
class Cell:
    def __init__(self, gameDisplay, c, r, state=0):
        self.c = c
        self.r = r
        self.state = state
        self.gameDisplay = gameDisplay

    def display(self):
        if self.state == 1:
            pygame.draw.rect(
                self.gameDisplay,
                BLACK,
                [SIZE_C * self.r, SIZE_C * self.c, SIZE_C, SIZE_C],
            )
        else:
            pygame.draw.rect(
                self.gameDisplay,
                WHITE,
                [SIZE_C * self.r, SIZE_C * self.c, SIZE_C, SIZE_C],
            )

    def checkNeighbors(self, cellList):
        neighbs = 0
        # Check for all
        for dr, dc in [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [1, 0],
            [1, -1],
            [1, 1],
            [0, -1],
            [0, 1],
        ]:
            try:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in [2, 3]:
                return 1
            return 0
        if neighbs == 3:
            return 1
        return 0
