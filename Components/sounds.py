import pygame

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

# Sound variables (Supports wav and ogg files)
pongSound = pygame.mixer.Sound('./media/pong.ogg')
scoreSound = pygame.mixer.Sound('./media/score.ogg')
shrinkSound = pygame.mixer.Sound('./media/shrink.wav')
slowDownSound = pygame.mixer.Sound('./media/slowDown.wav')
fastBallSound = pygame.mixer.Sound('./media/fastBall.wav')
inverseControlSound = pygame.mixer.Sound('./media/inverseControls.wav')
growSound = pygame.mixer.Sound('./media/grow.wav')
speedUpPaddleSound = pygame.mixer.Sound('./media/speedUpPaddle.wav')


def playPongSound():
    pygame.mixer.Sound.play(pongSound)


def playScoreSound():
    pygame.mixer.Sound.play(scoreSound)


def playGrowSound():
    pygame.mixer.Sound.play(growSound)


def playShrinkSound():
    pygame.mixer.Sound.play(shrinkSound)


def playSlowDownSound():
    pygame.mixer.Sound.play(slowDownSound)


def playFastBallSound():
    pygame.mixer.Sound.play(fastBallSound)


def playInverseControlSound():
    pygame.mixer.Sound.play(inverseControlSound)


def playSpeedUpSound():
    pygame.mixer.Sound.play(speedUpPaddleSound)
