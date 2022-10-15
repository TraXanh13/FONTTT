import pygame
import random


class Ball:
    def getBall(self):
        return self.ball

    def changeBallSpeed(self, speedX, speedY):
        if (self.getBallDirection):
            self.ballSpeedX = speedX + random.randint(0, 3)
            self.ballSpeedY = speedY + random.randint(0, 3)
        else:
            self.ballSpeedX = speedX + random.randint(-3, 0)
            self.ballSpeedY = speedY + random.randint(-3, 0)

    def drawBall(self):
        pygame.draw.ellipse(self.screen, self.color, self.ball)

    def moveBall(self):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Bounce off top and bottom
        if (self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height()):
            self.ballSpeedY *= -1

    def getSpeedX(self):
        return self.ballSpeedX

    def getSpeedY(self):
        return self.ballSpeedY
