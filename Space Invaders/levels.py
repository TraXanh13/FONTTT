import pygame
import math
import random
import json
import sys

f = open('config.json')
data = json.load(f)


class Levels():
    def __init__(self, screen):
        self.lvState = "level1"
        self.screen = screen
        self.levels = []

        # Player
        self.playerImg = pygame.image.load("./media/spaceship.png")
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0

        # Enemy
        self.enemyImg = []
        self.enemyUFOs = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.enemySpeed = 4
        self.score_value = 1
        self.num_enemies = 6

        # Bullet
        self.bulletImg = pygame.image.load("./media/bullet.png")
        self.bullet_sound = pygame.mixer.Sound("./media/laser.wav")
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = "ready"

        # Score Board
        self.score_value = 0
        self.level_complete_value = 0
        self.font = pygame.font.Font("./fonts/Square.ttf", 24)
        self.textX = 10
        self.textY = 10

        # Game Over Text
        # create the font for game over
        self.game_over_font = pygame.font.Font("./fonts/Square.ttf", 128)
        self.try_again_font = pygame.font.Font("./fonts/Square.ttf", 50)

        # flags
        self.gameOverFlag = False
        self.initLevelFlag = True
        self.running = True

        # Background stuff
        self.background = pygame.image.load("./media/stars.png")

    # The different game states

    def gameState(self):
        if (self.lvState == "level1"):
            self.level1()
        elif (self.lvState == "level2"):
            self.level2()

    # Returns whether the game is still running or not
    def isRunning(self):
        return self.running

    # Configures the level
    def initLevel(self, level):
        self.playerImg = pygame.image.load(data['levels'][level]['playerImg'])
        self.bullet_sound = pygame.mixer.Sound(
            data['levels'][level]['bulletSound'])
        self.background = pygame.image.load(
            data['levels'][level]['backgroundImg'])
        self.num_enemies = data['levels'][level]['numberOfEnemies']
        self.enemySpeed = data['levels'][level]['enemySpeed']
        self.level_complete_value = data['levels'][level]['levelCompleteValue']

        pygame.mixer.music.load(data['levels'][level]['backgroundMusic'])
        pygame.mixer.music.play(-1)
        self.createEnemies(data['levels'][level]['enemyUFOs'])

    # Creates the enemies for the level
    def createEnemies(self, ufos=["./media/ufo.png"]):
        self.enemyImg.clear()
        self.enemyX.clear()
        self.enemyY.clear()
        for i in range(self.num_enemies):
            self.enemyImg.append(pygame.image.load(random.choice(ufos)))
            self.enemyX.append(random.randint(0, 735))
            self.enemyY.append(random.randint(50, 150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)

    def show_score(self, x, y):
        score = self.font.render(
            "Score: "+str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def player(self, x, y):
        self.screen.blit(self.playerImg, (x, y))

    def enemy(self, x, y, i):
        self.screen.blit(self.enemyImg[i], (x, y))

    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (x+16, y+10))

    def isCollision(self, enemyX, enemyY, bulletX, bulletY):

        distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
                             math.pow(enemyY-bulletY, 2))

        if distance < 27:
            return True
        else:
            return False

    def game_over(self):  # display the game over text
        over_font = self.game_over_font.render(
            "GAME OVER", True, (255, 255, 255))
        try_again = self.try_again_font.render(
            "Press Space to Try Again", True, (255, 255, 255))
        self.screen.blit(over_font, (100, 250))
        self.screen.blit(try_again, (110, 360))

    def level1(self):
        if (self.initLevelFlag == True):
            # Set up level
            self.initLevel("1")
            self.initLevelFlag = False

        # Game Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.playerX_change = -3

                if event.key == pygame.K_RIGHT:
                    self.playerX_change = 3

                if event.key == pygame.K_SPACE:
                    if self.bullet_state == "ready":
                        self.bullet_sound.play()
                        self.bulletX = self.playerX
                        self.fire_bullet(self.bulletX, self.bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.playerX_change = 0

            if self.gameOverFlag == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gameOverFlag = False
                        self.score_value = 0
                        self.level1()

        # Screen Attributes
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        self.playerX += self.playerX_change

        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

        # Enemy Movement
        for i in range(self.num_enemies):

            # Game Over
            if self.enemyY[i] > 440:  # trigger the end of the game
                for j in range(self.num_enemies):
                    self.enemyY[j] = 2000
                self.gameOverFlag = True

            if self.gameOverFlag == True:
                self.game_over()
            else:
                self.enemyX[i] += self.enemyX_change[i]
                if self.enemyX[i] <= 0:
                    self.enemyX_change[i] = 4
                    self.enemyY[i] += self.enemyY_change[i]
                elif self.enemyX[i] >= 736:
                    self.enemyX_change[i] = -4
                    self.enemyY[i] += self.enemyY_change[i]

                collision = self.isCollision(
                    self.enemyX[i], self.enemyY[i], self.bulletX, self.bulletY)
                if collision:
                    explosion_sound = pygame.mixer.Sound(
                        "./media/explosion.wav")
                    explosion_sound.play()
                    self.bulletY = 480
                    self.bullet_state = "ready"
                    self.score_value += 1
                    self.enemyX[i] = random.randint(0, 800)
                    self.enemyY[i] = random.randint(50, 150)

            self.enemy(self.enemyX[i], self.enemyY[i], i)

        # Bullet Animation
        if self.bulletY <= 0:
            self.bulletY = 480
            self.bullet_state = "ready"

        if self.bullet_state == "fire":
            self.fire_bullet(self.bulletX, self.bulletY)
            self.bulletY -= self.bulletY_change

        self.player(self.playerX, self.playerY)
        self.show_score(self.textX, self.textY)

        if (self.score_value == 5):
            self.lvState = "level2"
            self.initLevelFlag = True
            self.score_value += self.level_complete_value

    def level2(self):
        if (self.initLevelFlag == True):
            # Set up level
            self.initLevel("2")
            self.initLevelFlag = False

        # Game Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.playerX_change = -3

                if event.key == pygame.K_RIGHT:
                    self.playerX_change = 3

                if event.key == pygame.K_SPACE:
                    if self.bullet_state == "ready":
                        self.bullet_sound.play()
                        self.bulletX = self.playerX
                        self.fire_bullet(self.bulletX, self.bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.playerX_change = 0

            if self.gameOverFlag == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gameOverFlag = False
                        self.score_value = 0
                        self.level1()

        # Screen Attributes
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        self.playerX += self.playerX_change

        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

        # Enemy Movement
        for i in range(self.num_enemies):

            # Game Over
            if self.enemyY[i] > 440:  # trigger the end of the game
                for j in range(self.num_enemies):
                    self.enemyY[j] = 2000
                self.gameOverFlag = True

            if self.gameOverFlag == True:
                self.game_over()
            else:
                self.enemyX[i] += self.enemyX_change[i]
                if self.enemyX[i] <= 0:
                    self.enemyX_change[i] = 4
                    self.enemyY[i] += self.enemyY_change[i]
                elif self.enemyX[i] >= 736:
                    self.enemyX_change[i] = -4
                    self.enemyY[i] += self.enemyY_change[i]

                collision = self.isCollision(
                    self.enemyX[i], self.enemyY[i], self.bulletX, self.bulletY)
                if collision:
                    explosion_sound = pygame.mixer.Sound(
                        "./media/explosion.wav")
                    explosion_sound.play()
                    self.bulletY = 480
                    self.bullet_state = "ready"
                    self.score_value += 1
                    self.enemyX[i] = random.randint(0, 800)
                    self.enemyY[i] = random.randint(50, 150)

            self.enemy(self.enemyX[i], self.enemyY[i], i)

        # Bullet Animation
        if self.bulletY <= 0:
            self.bulletY = 480
            self.bullet_state = "ready"

        if self.bullet_state == "fire":
            self.fire_bullet(self.bulletX, self.bulletY)
            self.bulletY -= self.bulletY_change

        self.player(self.playerX, self.playerY)
        self.show_score(self.textX, self.textY)
