from turtle import screensize
import pygame

pygame.font.init()

# Global Variables
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
light_grey = (200, 200, 200)

def increase_player_score():
    global player_score
    player_score += 1

def increase_opponent_score():
    global opponent_score
    opponent_score += 1

def draw_scores(screen, screen_width, screen_height):
    global light_grey
    player_text = basic_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (screen_width/2 + 50, screen_height/2))

    opponent_text = basic_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (screen_width/2 - 70, screen_height/2))
