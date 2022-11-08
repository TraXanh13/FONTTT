import pygame
import levels

pygame.init()
clock = pygame.time.Clock()                               

# Game Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Sound
pygame.mixer.music.load("./media/background_1.wav")
pygame.mixer.music.play(-1)

# Init level
lv = levels.Levels(screen)
lv.createEnemies()                     

#Init Main Menu Components
background = pygame.image.load("./media/stars.png")
main_font = pygame.font.Font('./fonts/Square.ttf', 75)
second_font = pygame.font.Font("./fonts/Square.ttf", 50)
main_text = "SPACE INVADERS"
second_text = "Press the space key to start"

#Welcome Screen
menuRunning = True
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))

#Space Invaders Title
main_text_display = main_font.render(main_text, True, (255, 255, 255))
text_rect = main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
screen.blit(main_text_display, text_rect)

#Instruction Text
second_main_text_display = second_font.render(second_text, True, (255, 255, 255))
text_rect2 = second_main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 55))
screen.blit(second_main_text_display, text_rect2)

pygame.display.update()
while menuRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menuRunning = False
                
# Game Loop
while lv.isRunning():
    if(lv.isOnCurrentStage()):
        lv.gameState()
        pygame.display.update()
        clock.tick(60)
    else:
        lv.stageScreen()
        pygame.display.update()
        pygame.time.wait(3000)
        lv.currentStage = True
