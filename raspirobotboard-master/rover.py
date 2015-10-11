from raspirobotboardcar import *
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
            if event.key == K_q:
                rr.forwardleft()
            elif event.key == K_w:
                rr.forward()
            elif event.key == K_e:
                rr.forwardright()
            elif event.key == K_a:
                rr.reverseleft()
            elif event.key == K_s:
                rr.reverse()
            elif event.key == K_d:
                rr.reverseright()
            elif event.key == K_SPACE:
                rr.stop()
