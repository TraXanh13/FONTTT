import pygame
import Components.character as character


class Opponent(character.Character):
    def __init__(self, screen):
        self.speed = 6
        self.defaultSpeed = 6
        self.character = pygame.Rect(
            20, screen.get_height()/2-70, 10, 140)
        self.screen = screen

    # Moves the opponent to follow the ball
    def moveOpponent(self, ball):
        if ball.y > self.character.y:
            self.character.y += self.speed
            if self.character.bottom >= self.screen.get_height():
                self.character.bottom = self.screen.get_height()
        if ball.y < self.character.y:
            self.character.y -= self.speed
            if self.character.top <= 0:
                self.character.top = 0
