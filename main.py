import pygame
from snake import *

pygame.init()
bounds = (300,300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("SNEK")

block_size = 20
snake = Snake(block_size, bounds)

