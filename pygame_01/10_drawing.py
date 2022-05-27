# -*- coding: utf-8 -*-
from operator import truediv
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("민재is태민")

clock = pygame.time.Clock()

running = True
while running:      
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.fill((255, 255, 255))

    # pygame.draw.line(screen, (100, 234, 136), (0, 0), (screen_width, screen_height), 30)
    # pygame.draw.line(screen, (255, 255, 13), (0, screen_height), (screen_width, 0), 30)

    for i in range(0, 480, 30):
        pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 640))
    for i in range(0, 640, 30):
        pygame.draw.line(screen, (0, 0, 255), (0, i), (480, i))

    # pygame.draw.circle(screen, (130, 155, 200), (screen_width / 2, screen_height / 2), 100)
    # pygame.draw.circle(screen, (5, 5, 5), (screen_width / 2, screen_height / 2), 100, 5)

    # pygame.draw.rect(screen, (215, 125, 255), (screen_width / 2, screen_height / 2, 100, 100))
    # pygame.draw.rect(screen, (55, 15, 55), (screen_width / 2, screen_height / 2, 100, 200), 5)

    # pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 100))
    # pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, 100, 100), 5)


    # pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2, screen_height / 2 - 100, 100, 100))
    # pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2, screen_height / 2 - 100, 100, 100), 5)

    # pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 200], [200, 200]])
    # pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], [100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100], ])


    pygame.display.update()

pygame.quit()