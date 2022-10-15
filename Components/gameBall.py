import pygame
import random
import mods
import Components.ball as ball
import Components.sounds as sounds
# import Components.itemBox as itemBox

modList = [mods.inverseControls, mods.shrinkPaddle,
           mods.growPaddle, mods.slowMotion, mods.speedUp, mods.fastBall]


class GameBall(ball.Ball):
    def __init__(self, screen):
        self.ball = pygame.Rect(screen.get_width()/2-15,
                                screen.get_height()/2-15, 30, 30)
        self.ballSpeedX = 7
        self.ballSpeedY = 7
        self.maxX = screen.get_width()
        self.maxY = screen.get_height()
        self.screen = screen
        self.color = (255, 255, 255)

    def getBallDirection(self):
        if (self.ballSpeedX > 0):
            return True
        return False

    def resetBall(self):
        self.ball.x = self.maxX/2-15
        self.ball.y = self.maxY/2-15
        self.ballSpeedX *= random.choice((1.25, 1, 0.75, -0.75, - 1, -1.25))
        self.ballSpeedY *= random.choice((1.25, 1, 0.75, -0.75, -1, -1.25))

    def changeBallSpeed(self, speed):
        if (self.getBallDirection):
            self.ballSpeedX = speed + random.randint(0, 3)
            self.ballSpeedY = speed + random.randint(0, 3)
        else:
            self.ballSpeedX = speed + random.randint(-3, 0)
            self.ballSpeedY = speed + random.randint(-3, 0)

    # Overrides the parent ball method
    def moveBall(self, player, opponent, itemBox, score):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Ball Collision with top and bottom of screen
        if (self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height()):
            self.ballSpeedY *= -1

        # Reaching the left side of the screen
        if (self.ball.left <= 0):
            sounds.playScoreSound()
            self.resetBall()
            player.resetCharacter()
            opponent.resetCharacter()
            score.increase_player_score()

        # Reaching the right side of the screen
        if (self.ball.right >= self.screen.get_width()):
            sounds.playScoreSound()
            self.resetBall()
            player.resetCharacter()
            opponent.resetCharacter()
            score.increase_opponent_score()

        # Bounce off player
        if (self.ball.colliderect(player.getCharacter())):
            sounds.playPongSound()
            self.ballSpeedX *= -1
            if (self.ball.y > player.getCharacter().centery + 20):
                self.ballSpeedY = abs(self.ballSpeedY)
            elif (self.ball.y < player.getCharacter().centery - 20):
                self.ballSpeedY = -abs(self.ballSpeedY)

        # Bounce off opponent
        if (self.ball.colliderect(opponent.getCharacter())):
            sounds.playPongSound()
            self. ballSpeedX *= -1
            if (self.ball.y > opponent.getCharacter().centery + 20):
                self.ballSpeedY = abs(self.ballSpeedY)
            elif (self.ball.y < opponent.getCharacter().centery - 20):
                self.ballSpeedY = -abs(self.ballSpeedY)

        if (self.ball.colliderect(itemBox.getBox())):
            itemBox.removeBox()
            modList[random.randint(0, len(modList)-1)](player, opponent, self)
