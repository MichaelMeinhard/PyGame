import pygame
import os

from classes.slash import Slash

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))

# Image's Load
left = [None]*10
for picIndex in range(1,10):
    left[picIndex-1] = pygame.image.load(os.path.join("hero", "L" + str(picIndex) + ".png"))
    picIndex+=1

right = [None]*10
for picIndex in range(1,10):
    right[picIndex-1] = pygame.image.load(os.path.join("hero", "R" + str(picIndex) + ".png"))
    picIndex+=1


class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False
        # Slash
        self.slashes = []

    # Hero's movement
    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    # Portayal of the hero
    def draw(self, win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    # Jump motion
    def jump_motion(self, userInput):
        if userInput[pygame.K_UP] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vel_y*4
            self.vel_y -= 1
        if self.vel_y < -10:
            self.jump = False
            self.vel_y = 10

    def slash(self, userInput):
        if userInput[pygame.K_SPACE]:
            slash = Slash(self.x, self.y)