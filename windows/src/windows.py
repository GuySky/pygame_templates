from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'     # get rid of console

import pygame

pygame.init()



# ----====  16:9  ====----
# common resolutions:
# 320, 180
# 640, 360

# -> scale to:
# 1280, 720
# 1920, 1080
# 2048, 1080
# 3840, 2160
SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
# ----====XXXXXXXX====----



# ----====  display flags   ====----
# pygame.RESIZABLE  -   borders of the window can be dragged to chenge its size
# pygame.SCALED     -   resolution depends on desktop size
# pygame.FULLSCREEN -   always fullscreen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()
# ----====XXXXXXXX====----



icon = pygame.image.load('windows/assets/images/icon.png').convert_alpha()      # window icon
bg_image = pygame.image.load('windows/assets/images/bg1.png').convert_alpha()   # background image

pygame.display.set_icon(icon)
pygame.display.set_caption('windows template')      # window caption

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.blit(bg_image)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()