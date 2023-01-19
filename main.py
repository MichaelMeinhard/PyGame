import pygame
from classes.hero import *
from classes.slash import *
from classes.enemy import Enemy

pygame.init()

bg_img = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg_img, (1280, 720))


def draw_game():
    win.blit(bg, (0,0))
    player.draw(win)
    for slh in player.slashes:
        if slh.shouldDelete:
            player.slashes.remove(slh)

    for slh in player.slashes:
        slh.draw()
    for ene in enemies:
        ene.draw(win)
    pygame.time.delay(30)
    pygame.display.update()


player = Hero(win_width/2, 525)
enemies = []

# Main
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    player.move_hero(userInput)
    player.jump_motion(userInput)
    player.slash(userInput)

    if len(enemies) == 0:
        enemy = Enemy(win_width + 20, 530)
        enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        player.damage(enemy)
    for enemy in enemies:
        if enemy.to_delete:
            enemies.remove(enemy)
        for sl in player.slashes:
            enemy.damage(sl)
        if enemy.off_screen():
            enemies.remove(enemy)

    draw_game()