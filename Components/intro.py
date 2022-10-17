import pygame
import Components.sounds as sounds

pygame.font.init()

light_grey = (200, 200, 200)
basic_font = pygame.font.Font('freesansbold.ttf', 200)
small_font = pygame.font.Font('freesansbold.ttf', 50)
played = False


def intro_scene(screen, screen_width, screen_height):
    global light_grey
    global played
    if played == False:
        sounds.playIntroSound()
    title = basic_font.render(f"PONG", False, light_grey)
    starttext = small_font.render(f"Press Up Arrow to Play", False, light_grey)
    quittext = small_font.render(f"Press ESC to Quit", False, light_grey)

    text_rect = title.get_rect(center=(screen_width/2, screen_height/2))
    quit_text_rect = quittext.get_rect(
        center=(screen_width/2, screen_height/2 + 250))
    start_text_rect = starttext.get_rect(
        center=(screen_width/2, screen_height/2 + 150))

    screen.blit(title, text_rect)
    screen.blit(starttext, start_text_rect)
    screen.blit(quittext, quit_text_rect)
    played = True