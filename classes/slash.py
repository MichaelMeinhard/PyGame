import pygame
import os

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))

# Image's Load
slash = [None]*7
for picIndex in range(1,7):
    slash[picIndex-1] = pygame.image.load(os.path.join("slashes", "Slash" + str(picIndex) + ".png"))
    picIndex+=1


class Slash:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
            win.blit(slash, (self.x, self.y))