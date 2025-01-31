from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()

icon = pygame.image.load('windows/assets/images/icon.png')

pygame.display.set_icon(icon)

pygame.display.set_caption('windows template')

screen = pygame.display.set_mode((1280, 720), vsync=1)

clock = pygame.time.Clock()
running = True

pygame.display.toggle_fullscreen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()