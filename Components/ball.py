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
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        ORANGE = (255, 165, 0)
        RED = (255, 0, 0)
        
        # Ball changes color depending on speed
        if(self.getSpeedX() < 7 and self.getSpeedX() > -7):
            pygame.draw.ellipse(self.screen, BLUE, self.ball)
        elif(self.getSpeedX() == 7 or self.getSpeedX() == -7):
            pygame.draw.ellipse(self.screen, self.color, self.ball)
        elif(( self.getSpeedX() > -10 and self.getSpeedX() < -7) or (self.getSpeedX() < 10 and self.getSpeedX() > 7)):
            pygame.draw.ellipse(self.screen, YELLOW, self.ball)
        elif((self.getSpeedX() >= -12.5 and self.getSpeedX() <= -10) or (self.getSpeedX() <= 12.5 and self.getSpeedX() >= 10)):    
            pygame.draw.ellipse(self.screen, ORANGE, self.ball)
        else:
            pygame.draw.ellipse(self.screen, RED, self.ball)

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
