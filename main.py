import pygame
from classes.hero import *
from classes.slash import *

pygame.init()

bg_img = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg_img,(1280, 720))


def draw_game():
    win.blit(bg, (0,0))
    player.draw(win)
    for slash in player.slashes:
        slash.draw()
    pygame.time.delay(30)
    pygame.display.update()

player = Hero(win_width/2, 525)

# Main
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    player.move_hero(userInput)
    player.jump_motion(userInput)

    draw_game()