# Conway's Game of Life - Python Implementation
# Author: Daniel: dan@imdany.com

import pygame
from pygame.locals import *
from cell import Cell
from config import *
import time
from random import choice

# Initialising PyGame
pygame.init()
pygame.display.set_caption("PyConway")
gameDisplay = pygame.display.set_mode((MAX_W, MAX_H))
clock = pygame.time.Clock()

# Initialise the Grid as random
# TODO: Add an easy way of setting up situations
def createCellList():
    newList = []
    # Populate Initial
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList[j].append(Cell(gameDisplay, i, j, choice([0, 1])))
    return newList


# Logic for updating the board on each generation
def update(cellList):
    newList = []
    for r, row in enumerate(cellList):
        newList.append([])
        for c, cell in enumerate(row):
            newList[r].append(Cell(gameDisplay, r, c, cell.checkNeighbors(cellList)))
    return newList[::]


def main():
    generation = 0
    cellList = createCellList()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    running = False

        # Remove all previous content on the board
        gameDisplay.fill(BLACK)

        # Calculate the new state of the board
        cellList = update(cellList)

        # Display each Cell
        for row in cellList:
            for cell in row:
                cell.display()

        generation = generation + 1

        # Three Frames per second
        clock.tick(3)
        pygame.display.flip()
        print(f"Generation: {generation}")

    pygame.quit()


if __name__ == "__main__":
    main()
