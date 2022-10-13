import pygame
import random

# Item Box Variables
box_height = 30
box_width = 30
box_x = 1500
box_y = 0


def spawnBox(clock):
    global box_x, box_y
    if (clock % 4000 <= 17):
        box_x = random.randint(50, 1150)
        box_y = random.randint(0, 670)
    return pygame.Rect(box_x, box_y, box_height, box_width)


def getBox():
    return pygame.Rect(box_x, box_y, box_height, box_width)


def removeBox():
    global box_x, box_y
    box_x = 1500
    box_y = 0
