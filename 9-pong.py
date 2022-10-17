from asyncio.windows_events import NULL
import pygame
import sys
import Components.score as score
import Components.itemBox as itemBox
import Components.multiplayer as multiplayer
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
player = Player(screen, pygame.Rect(screen.get_width()-20, screen.get_height()/2-70, 10, 140))
#set to null after
#op = Opponent(screen)
op = NULL
ball = GameBall(screen)
player_two = NULL 


def  playerMovement():
    # Controlled with the up and down arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_DOWN]:
        player.moveDown() 
    return

def secondPlayerMovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_two.moveUp()
    if keys[pygame.K_s]:
        player_two.moveDown()
    return

multiplayer.init(screen)
if(multiplayer.isMultiplayerSelected()):
    player_two = multiplayer.getPlayerTwo()
else:
    op = multiplayer.getOp()    

if __name__ == "__main__":
    # Game loop
    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        # Move objects
        if(multiplayer.isMultiplayerSelected()):
            secondPlayerMovement()
            ball.moveBall(player, player_two, itemBox, score)
        else: 
            ball.moveBall(player, op, itemBox, score)
            op.moveOpponent(ball.getBall())
        playerMovement()
        # Draw objects
        screen.fill(bgColor)
        pygame.draw.aaline(screen, lightGrey, (screenWidth/2,
                           0), (screenWidth/2, screenHeight))
        player.drawCharacter("p")
        if (not multiplayer.isMultiplayerSelected()):
            op.drawCharacter("op")
        else:
            player_two.drawCharacter("p")
        ball.drawBall()
        pygame.draw.rect(screen, (255, 255, 255),
                         itemBox.spawnBox(pygame.time.get_ticks()))

        # Update scores
        score.draw_scores(screen, screenWidth, screenHeight)

        if(multiplayer.isMultiplayerSelected()):
            ball.moveBall(player, player_two, itemBox, score)
        else: 
            ball.moveBall(player, op, itemBox, score)

        # updating the window
        pygame.display.flip()
        clock.tick(60)
