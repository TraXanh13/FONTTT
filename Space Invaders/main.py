import pygame
import math
import random
import levels

pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Sound
pygame.mixer.music.load("./media/background.wav")
pygame.mixer.music.play(-1)

# Init level
lv = levels.Levels(screen)
lv.createEnemies()

# Game Loop
running = True
while running:
    lv.level1()
    pygame.display.update()
