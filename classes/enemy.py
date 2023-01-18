import pygame
import os

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))


enemy_l = [None]*11
for picIndex in range(0,11):
    enemy_l[picIndex] = pygame.image.load(os.path.join("enemy", "L" + str(picIndex + 1) + ".png"))

enemy_r = [None]*11
for picIndex in range(0,11):
    enemy_r[picIndex] = pygame.image.load(os.path.join("enemy", "R" + str(picIndex + 1) + ".png"))


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stepIndex = 0
        self.max_health = 100
        self.health = 100

    def step(self):
        if self.stepIndex >= 33:
            self.stepIndex = 0

    def off_screen(self):
        return not(self.x >= -20 and self.x <= win_width + 20)

    def draw(self, win):

        self.step()
        win.blit(enemy_l[self.stepIndex//3], (self.x, self.y))
        self.stepIndex += 1


    def move(self):
        self.x -= 3
