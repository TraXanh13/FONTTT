import pygame
import Components.score as score

class Character:

    def getCharacter(self):
        return self.character

    def drawCharacter(self, string):
        if(score.opponent_score % 2 != 0 and string is 'p'):
            pygame.draw.rect(self.screen, (40, 40, 40), self.character)
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
