import pygame
import Components.score as score

class Character:

    def getCharacter(self):
        return self.character

    #Transparent Mod: Every time a player/opponent scores, the opposite player will have an almost transparent bar instead
    #This awards the scoring player, while punishing the losing player at the same time.
    #Although it might be punishing, it can encourage the losing player to focus and work on their predictions to be able score.
    def drawCharacter(self, string):
        if(score.opponent_scored == True):
            if(string == 'p'):
                pygame.draw.rect(self.screen, (40, 40, 40), self.character)
            else:
                pygame.draw.rect(self.screen, (200, 200, 200), self.character)
        elif(score.player_scored == True):
            if(string == 'op'):
                pygame.draw.rect(self.screen, (40, 40, 40), self.character)
            else:
                pygame.draw.rect(self.screen, (200, 200, 200), self.character)
        else:
            pygame.draw.rect(self.screen, (200, 200, 200), self.character)
            
    def resetSpeed(self):
        self.speed = self.defaultSpeed

    def resetHeight(self):
        self.character.inflate_ip(0, 140-self.character.height)

    def resetCharacter(self):
        self.resetSpeed()
        self.resetHeight()

    def changeSpeed(self, speed):
        self.speed = speed

    def getHeight(self):
        return self.character.height

    def getSpeed(self):
        return self.speed

    def changeHeight(self, height):
        self.character.inflate_ip(0, height)
