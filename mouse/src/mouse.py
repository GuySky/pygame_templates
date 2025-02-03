from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()

icon = pygame.image.load('mouse/assets/images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption('mouse template')

cursor = pygame.image.load('mouse/assets/images/cursor.png').convert_alpha()
CURSOR_SIZE = (21, 21)

cursor = pygame.transform.scale(cursor, CURSOR_SIZE)
cursor = pygame.cursors.Cursor((CURSOR_SIZE[0] // 2 + 1, CURSOR_SIZE[1] // 2 + 1), cursor)
pygame.mouse.set_cursor(cursor)

clock = pygame.time.Clock()
running = True

cursor_index = 0
cursors = [cursor, pygame.cursors.arrow]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_index += 1
            cursor_index %= len(cursors)
            pygame.mouse.set_cursor(cursors[cursor_index])

    screen.fill((197, 127, 214))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()