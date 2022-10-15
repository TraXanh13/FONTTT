import pygame

# Sound Variables


def initMixer():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    global score_sound
    score_sound = pygame.mixer.Sound("./media/score.ogg")
    global pong_sound
    pong_sound = pygame.mixer.Sound("./media/pong.ogg")
    global alien_sound
    alien_sound = pygame.mixer.Sound("./media/alien-8bit.wav")


def scoreSound():
    pygame.mixer.Sound.play(score_sound)


def pongSound():
    pygame.mixer.Sound.play(pong_sound)


def alienSound():
    pygame.mixer.Sound.play(alien_sound)
