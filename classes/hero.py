import pygame
import os

from classes.slash import Slash

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))

# Image's Load
left = [None] * 9
for picIndex in range(0, 9):
    left[picIndex] = pygame.image.load(os.path.join("hero", "L" + str(picIndex + 1) + ".png"))

right = [None] * 9
for picIndex in range(0, 9):
    right[picIndex] = pygame.image.load(os.path.join("hero", "R" + str(picIndex + 1) + ".png"))


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
        self.max_health = 100
        self.health = 100
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
        # Movement
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

        # Health
        pygame.draw.rect(win, (0, 0, 0), (self.x + 11, self.y - 1, 35, 12))
        pygame.draw.rect(win, (255 - ((self.health / self.max_health) * 255), (self.health / self.max_health) * 255, 0),
                         (self.x + 12, self.y, 33, 10))

    # Jump
    def jump_motion(self, userInput):
        if userInput[pygame.K_UP] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vel_y * 4
            self.vel_y -= 1
        if self.vel_y < -10:
            self.jump = False
            self.vel_y = 10

    def slash(self, userInput):
        if userInput[pygame.K_SPACE]:
            if len(self.slashes) == 0:
                slash = Slash(self.x + 15, self.y + 5, self.face_left)
                self.slashes.append(slash)
            elif self.slashes[len(self.slashes) - 1].time > 5:
                slash = Slash(self.x + 15, self.y + 5, self.face_left)
                self.slashes.append(slash)

    def damage(self, enemy):
        if enemy.x - 15 < self.x < enemy.x + 15 and enemy.y - 20 < self.y < enemy.y:
            self.health -= 5