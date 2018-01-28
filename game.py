import pygame
import sys

WINDOW_HEIGHT = 1920
WINDOW_WIDTH = 1080
size = WINDOW_HEIGHT, WINDOW_WIDTH
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kunkka's Plunder")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 128), (0, 0, 100, 100))
    pygame.display.flip()
