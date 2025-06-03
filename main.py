import pygame
import time
import math

GRASS = pygame.image.load("imgs/grass.jpg")
TRACK = pygame.image.load("imgs/track.png")

TRACK_BORDER = pygame.image.load("imgs/track-border.png")
FINISH = pygame.image.load("imgs/finish.png")

PURPLE_CAR = pygame.image.load("imgs/purple-car.png")
GREEN_CAR = pygame.image.load("imgs/green-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")