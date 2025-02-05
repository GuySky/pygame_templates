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


CURSOR_SIZE = (21, 21)
cursors = [
    pygame.cursors.Cursor(
        (CURSOR_SIZE[0] // 2 + 1, CURSOR_SIZE[1] // 2 + 1),
        pygame.transform.scale(pygame.image.load(f'mouse/assets/images/cursors/cursor{i}.png').convert_alpha(), CURSOR_SIZE)
    ) 
    for i in range(1, 5)
]

CURSOR_INDEX = 0
pygame.mouse.set_cursor(cursors[CURSOR_INDEX])

clock = pygame.time.Clock()
running = True

is_animating = False
CURSOR_ANIMATION_DELAY = 5

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
            is_animating = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_animating = False
            CURSOR_INDEX = 0
            pygame.mouse.set_cursor(cursors[CURSOR_INDEX])

    if is_animating:
        CURSOR_INDEX = CURSOR_INDEX + 1
        pygame.mouse.set_cursor(cursors[(CURSOR_INDEX//CURSOR_ANIMATION_DELAY)%len(cursors)])

    screen.fill((197, 127, 214))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()