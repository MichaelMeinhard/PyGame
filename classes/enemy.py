import pygame
import os

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))

enemy_l = [None] * 11
for picIndex in range(0, 11):
    enemy_l[picIndex] = pygame.image.load(os.path.join("enemy", "L" + str(picIndex + 1) + ".png"))

enemy_r = [None] * 11
for picIndex in range(0, 11):
    enemy_r[picIndex] = pygame.image.load(os.path.join("enemy", "R" + str(picIndex + 1) + ".png"))


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stepIndex = 0
        self.max_health = 100
        self.health = 100
        self.to_delete = False
        self.speed = 10

    def step(self):
        if self.stepIndex >= 33:
            self.stepIndex = 0

    def off_screen(self):
        return not (self.x >= -20 and self.x <= win_width - 20)

    def draw(self, win):

        self.step()
        win.blit(enemy_l[self.stepIndex // 3], (self.x, self.y))
        self.stepIndex += 1

        # Health
        pygame.draw.rect(win, (0, 0, 0), (self.x + 21, self.y - 6, 35, 12))
        if self.health >= 0:
            pygame.draw.rect(win, (255 - ((self.health / self.max_health) * 255), (self.health / self.max_health) *
                                   255, 0), (self.x + 22, self.y - 5, (self.health / self.max_health) * 33, 10))

    def move(self):
        self.x -= self.speed

    def damage(self, slash):
        if slash.get_x() - 35 < self.x < slash.get_x() + 15 and slash.y - 20 < self.y < slash.y + 30:
            if slash.time == 0:
                self.health -= 50
            if self.health <= 0:
                self.to_delete = True
