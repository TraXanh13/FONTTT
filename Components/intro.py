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
    singleText = small_font.render(f"Press Down Arrow for Singleplayer", False, light_grey)
    multiText = small_font.render(f"Press Up Arrow for Multiplayer", False, light_grey)
    quittext = small_font.render(f"Press ESC to Quit", False, light_grey)

    text_rect = title.get_rect(center=(screen_width/2, screen_height/2 - 150))
    singleText_rect = multiText.get_rect(
        center=(screen_width/2, screen_height/2+75))
    multiText_rect = singleText.get_rect(
        center=(screen_width/2, screen_height/2 + 150))
    quit_text_rect = quittext.get_rect(
        center=(screen_width/2, screen_height/2 + 250))
    
    multiText_rect.centerx = screen_width/2 + 75
    singleText_rect.centerx = screen_width/2

    screen.blit(title, text_rect)
    screen.blit(singleText, singleText_rect)
    screen.blit(multiText, multiText_rect)
    screen.blit(quittext, quit_text_rect)
    played = True
