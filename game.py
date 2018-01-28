import pygame
import sys

size = 960,720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kunkka's Plunder")

# Test Comment
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 128), (0, 0, 100, 100))
    pygame.display.flip()
