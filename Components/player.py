import pygame
import Components.character as character


class Player(character.Character):
    def __init__(self, screen):
        self.speed = 10
        self.defaultSpeed = 10
        self.character = pygame.Rect(
            screen.get_width()-20, screen.get_height()/2-70, 10, 140)
        self.screen = screen

    def moveUp(self):
        self.character.y -= self.speed
        self.checkInbounds()

    def moveDown(self):
        self.character.y += self.speed
        self.checkInbounds()

    def checkInbounds(self):
        if (self.character.top <= 0):
            self.character.y = 0
        if (self.character.bottom > self.screen.get_height()):
            self.character.bottom = self.screen.get_height()
