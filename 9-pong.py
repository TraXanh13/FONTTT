import pygame
import sys
import Components.score as score
import Components.itemBox as itemBox
from Components.player import Player
from Components.opponent import Opponent
from Components.gameBall import GameBall

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

# colors
bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)

# Setting up main window
screenWidth = 1200
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

# Initialize classes
player = Player(screen)
op = Opponent(screen)
ball = GameBall(screen)


def playerMovement():
    # Controlled with the up and down arrow keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player.moveDown()
        if event.key == pygame.K_UP:
            player.moveUp()
    return


if __name__ == "__main__":
    # Game loop
    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw objects
        screen.fill(bgColor)
        pygame.draw.aaline(screen, lightGrey, (screenWidth/2,
                           0), (screenWidth/2, screenHeight))
        player.drawCharacter()
        op.drawCharacter()
        ball.drawBall()
        pygame.draw.rect(screen, (255, 255, 255), itemBox.spawnBox(pygame.time.get_ticks()))

        # Update scores
        score.draw_scores(screen, screenWidth, screenHeight)

        # Move objects
        playerMovement()
        ball.moveBall(player, op, itemBox, score)
        op.moveOpponent(ball.getBall())

        # updating the window
        pygame.display.flip()
        clock.tick(60)
