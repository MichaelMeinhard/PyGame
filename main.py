import pygame
from classes.hero import Hero
from classes.slash import Slash
from classes.enemy import Enemy
from classes.settings import *
from classes.waves import Fu

pygame.init()


def end(userInput, text_score, textRect_score):
    win.fill((0, 0, 0))
    win.blit(text_end, textRect)
    win.blit(text_score, textRect_score)
    if userInput[pygame.K_r]:
        return True


def draw_game(userInput):
    win.blit(bg, (0, 0))
    player.draw(win)
    for slh in player.slashes:
        if slh.shouldDelete:
            player.slashes.remove(slh)

    for slh in player.slashes:
        slh.draw()

    for ene in enemies:
        ene.draw(win)

    if player.game_over():
        if end(userInput):
            player.__init__(win_width / 2, 525)
            enemies.clear()
            wavee.__init__()

    # Waves
    text_wave = font.render('Wave: ' + str(wavee.wave), True, (0, 0, 0))
    text_score = font.render('Your wave: ' + str(wavee.wave), True, (255, 255, 255))
    textRect_wave = text_wave.get_rect()
    textRect_score = text_score.get_rect()
    textRect_wave.center = (win_width // 2, 100)
    textRect_score.center = (win_width // 2, win_height // 2 + 40 )
    win.blit(text_wave, textRect_wave)

    pygame.time.delay(30)
    pygame.display.update()


player = Hero(win_width / 2, 525)
enemies = []

# Main
run = True
time = 0

wavee = Fu()

while run:
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()
    if not player.game_over():
        player.move_hero(userInput)
        player.jump_motion(userInput)
        player.slash(userInput)

        if time % 150 - (wavee.wave * 5) == 0:
            enemies.append(Enemy(win_width - 20, 530))
        if time % 150 == 0:
            wavee.wave += 1
        if time % 600 == 0:
            player.health = player.max_health
        if len(enemies) == 0:
            enemy = Enemy(win_width - 20, 530)
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
                enemy.speed *= -1

    draw_game(userInput)
