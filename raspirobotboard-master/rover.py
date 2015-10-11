from raspirobotboard-car import *
import pygame
from pygame.locals import *

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont("arial", 64)

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)


while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_Q:
                rr.forwardleft()
            elif event.key == K_W:
                rr.forward()
            elif event.key == K_E:
                rr.forwardright()
            elif event.key == K_A:
                rr.reverseleft()
            elif event.key == K_S:
                rr.reverse()
            elif event.key == K_D:
                rr.reverseright()
            elif event.key == K_SPACE:
                rr.stop()
