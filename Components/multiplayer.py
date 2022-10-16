import pygame
from asyncio.windows_events import NULL
from Components.player import Player
from Components.opponent import Opponent
#global vars
multiplayerSelected = False
op = NULL
player_two = NULL
screen = NULL

def init(screenIn):
    global op
    global player_two
    global multiplayerSelected
    screen = screenIn
    response = input('Single Player or Multiplayer? (Respond with S or M)  ')
    while True:
        if response.upper() == 'S':
            op = Opponent(screen)
            break
        elif response.upper() == 'M':
            multiplayerSelected = True
            player_two = Player(screen, pygame.Rect(20, screen.get_height()/2-70, 10, 140))
            break
        else:
            response = input('Single Player or Multiplayer? (Respond with S or M)')

def secondPlayerMovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_two.moveUp()
    if keys[pygame.K_s]:
        player_two.moveDown()
    return

def isMultiplayerSelected():
    return multiplayerSelected

def getOp():
    return op

def getPlayerTwo():
    return player_two