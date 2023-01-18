import pygame
import os
import math


# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))

# Image's Load
slash = [None] * 6
for picIndex in range(0, 6):
    slash[picIndex] = pygame.image.load(os.path.join("slashes", "Slash" + str(picIndex + 1) + ".png"))
    slash[picIndex] = pygame.transform.scale(slash[picIndex], (60, 60))


slash_l= [None] * 6
for picIndex in range(0, 6):
    slash_l[picIndex] = pygame.image.load(os.path.join("slashes", "Slash" + str(picIndex + 1) + ".png"))
    slash_l[picIndex] = pygame.transform.scale(slash[picIndex], (60, 60))
    slash_l[picIndex] = pygame.transform.flip(slash[picIndex], True, False)


class Slash():
    def __init__(self, x, y, slash_left):
        self.x = x
        self.y = y
        self.slash_left = slash_left
        self.time = 0
        self.shouldDelete = False

    def draw(self):
        if not self.slash_left:
            win.blit(slash[self.time//3], (self.x, self.y))
            self.time += 1
        elif self.slash_left:
            win.blit(slash_l[self.time//3], (self.x - 30, self.y))
            self.time += 1
        if math.floor(self.time / 3) >= len(slash) or math.floor(self.time / 3) >= len(slash_l):
            self.shouldDelete = True
