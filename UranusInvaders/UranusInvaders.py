#this doesn't do anything yet but if it doesn't return any errors it should work i think - Ramon

import sys, pygame, random
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = [0, 0, 0]
white = [255, 255, 255]

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont("monospace", 15)
pygame.display.set_icon(pygame.image.load("Assets/ball.png"))
pygame.display.set_caption("Uranus invaders")


screen.fill(white)

while True:
    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    pygame.display.update()
    clock.tick(15)