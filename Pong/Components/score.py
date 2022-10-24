import pygame

pygame.font.init()

# Global Variables
player_score = 0
opponent_score = 0
opponent_scored = False
player_scored = False
basic_font = pygame.font.Font('freesansbold.ttf', 32)
light_grey = (200, 200, 200)

def increase_player_score():
    global player_score
    global player_scored
    global opponent_scored
    player_score += 1
    player_scored = True
    opponent_scored = False

def increase_opponent_score():
    global opponent_score
    global opponent_scored
    global player_scored
    opponent_score += 1
    opponent_scored = True
    player_scored = False

def draw_scores(screen, screen_width, screen_height):
    global light_grey
    player_text = basic_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (screen_width/2 + 50, screen_height/2))

    opponent_text = basic_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (screen_width/2 - 70, screen_height/2))
