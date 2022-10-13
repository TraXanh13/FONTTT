from random import random
import pygame


class Ball:
    def getBall(self):
        return self.ball

    def changeBallSpeed(self, speed):
        self.ballSpeedX = speed + random.randint(-3, 10)
        self.ballSpeedY = speed + random.randint(-3, 10)

    def drawBall(self):
        pygame.draw.ellipse(self.screen, self.color, self.ball)

    def moveBall(self):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Bounce off top and bottom
        if (self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height()):
            self.ballSpeedY *= -1
