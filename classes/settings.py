import pygame

# Settings
win_height = 720
win_width = 1280
win = pygame.display.set_mode((win_width, win_height))
slash_speed = 2

# Background
bg_img = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg_img, (1280, 720))

# Fonts
pygame.font.init()

font = pygame.font.Font('arial.ttf', 32)
text_end = font.render('You died press R to restart.', True, (255, 255, 255))
textRect = text_end.get_rect()
textRect.center = (win_width // 2, win_height // 2)