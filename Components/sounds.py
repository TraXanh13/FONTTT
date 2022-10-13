import pygame

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

# Sound variables (Supports wav and ogg files)
pongSound = pygame.mixer.Sound('./media/pong.ogg')
scoreSound = pygame.mixer.Sound('./media/score.ogg')
alienSound = pygame.mixer.Sound('./media/alien-8bit.wav')


def playPongSound():
    pygame.mixer.Sound.play(pongSound)


def playScoreSound():
    pygame.mixer.Sound.play(scoreSound)


def playAlienSound():
    pygame.mixer.Sound.play(alienSound)
