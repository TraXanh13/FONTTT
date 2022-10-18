from asyncio.windows_events import NULL
import pygame
import sys
import Components.score as score
import Components.itemBox as itemBox
import Components.multiplayer as multiplayer
from Components.player import Player
from Components.opponent import Opponent
from Components.gameBall import GameBall
import Components.intro as intro

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
isMultiplayer = False
isPlaying = False
count = 0

def  playerMovement():
    # Controlled with the up and down arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_DOWN]:
        player.moveDown() 
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    return

def secondPlayerMovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_two.moveUp()
    if keys[pygame.K_s]:
        player_two.moveDown()
    return

multiplayer.init(screen, screenWidth, screenHeight)
if(multiplayer.isMultiplayerSelected()):
    player_two = multiplayer.getPlayerTwo()
    
else:
    op = multiplayer.getOp()    

def gamemodeResponse():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            multiplayer.multiplayerSelected(False)
        if event.key == pygame.K_m:
            multiplayer.multiplayerSelected(True)

def skipIntro():
    global count
    global isPlaying
    global isMultiplayer
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            multiplayer.setMultiplayer(True)
            isPlaying = True
        if event.key == pygame.K_DOWN:
            multiplayer.setMultiplayer(False)
            isPlaying = True
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()



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
        player.drawCharacter("p")
        
        ball.drawBall()
        pygame.draw.rect(screen, (255, 255, 255),
                        itemBox.spawnBox(pygame.time.get_ticks()))

        

         # plays intro title screen
        if not isPlaying:
            intro.intro_scene(screen, screenWidth, screenHeight)
            skipIntro()
            isMultiplayer = multiplayer.isMultiplayerSelected()


        # Update scores
        score.draw_scores(screen, screenWidth, screenHeight)

        if isPlaying:
            if isMultiplayer:
                player_two = multiplayer.getPlayerTwo()
                player_two.drawCharacter("p") 
                secondPlayerMovement()
                ball.moveBall(player, player_two, itemBox, score)
            else:
                op = multiplayer.getOp()
                op.drawCharacter("op")    
                ball.moveBall(player, op, itemBox, score)
                op.moveOpponent(ball.getBall())      
            
            score.draw_scores(screen, screenWidth, screenHeight)
            # Move objects
            playerMovement()


        # updating the window
        pygame.display.flip()
        clock.tick(60)
