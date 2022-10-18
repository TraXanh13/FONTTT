from pickle import TRUE
import pygame
from asyncio.windows_events import NULL
from Components.player import Player
from Components.opponent import Opponent
import Components.sounds as sounds
#global vars
multiplayerSelected = False
op = NULL
player_two = NULL
screen = NULL
light_grey = (200, 200, 200)
basic_font = pygame.font.Font('freesansbold.ttf', 200)
small_font = pygame.font.Font('freesansbold.ttf', 50)
screen_width = 0
screen_height = 0

def init(screenIn, screenWidth, screenHeight):
    global multiplayerSelected
    global screen
    global screen_width
    global screen_height
    global light_grey
    screen = screenIn
    screen_width = screenWidth
    screen_height = screenHeight
    
def isMultiplayerSelected():
    global op
    global player_two
    if multiplayerSelected:
        player_two = Player(screen, pygame.Rect(20, screen.get_height()/2-70, 10, 140))
    else:
        op = Opponent(screen)    
    return multiplayerSelected

def getOp():
    return op

def getPlayerTwo():
    return player_two

def setMultiplayer(selected):
    global multiplayerSelected
    multiplayerSelected = selected
