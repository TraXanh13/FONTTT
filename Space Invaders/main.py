import pygame
import levels

pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Sound
pygame.mixer.music.load("./media/background_1.wav")
pygame.mixer.music.play(-1)

# Init level
lv = levels.Levels(screen)
lv.createEnemies()

# Game Loop
while lv.isRunning():
    lv.gameState()
    pygame.display.update()
    clock.tick(60)
