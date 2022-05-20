# -*- coding: utf-8 -*-

import pygame
import random


pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("민재 피하기-코도폴레이")


clock = pygame.time.Clock()





bg = pygame.image.load("pygame_01/source/bg2.png")

character = pygame.image.load("pygame_01/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height / 2) - (character_height / 2)

to_y = 0
to_x = 0
character_speed = 50



enemy1 = pygame.image.load("pygame_01/source/enemy.png")

enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
enemy1_yPos = 0



enemy1_speed = 10




enemy2 = pygame.image.load("pygame_01/source/enemy.png")

enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_xPos = screen_width - enemy2_width
enemy2_yPos =random.randint(0, (screen_height - enemy2_height))



enemy2_speed = 10





enemy3 = pygame.image.load("pygame_01/source/enemy.png")

enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_xPos = random.randint(0, (screen_width - enemy3_width))
enemy3_yPos = screen_height - enemy3_height



enemy3_speed = 10




enemy4 = pygame.image.load("pygame_01/source/enemy.png")

enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_xPos = 0
enemy4_yPos = random.randint(0, (screen_height - enemy4_height))



enemy4_speed = 10







running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
          
            elif event.key == pygame.K_UP:
                to_y -= character_speed

            elif event.key == pygame.K_DOWN:
                to_y += character_speed



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xPos += to_x
    character_yPos += to_y

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos >screen_width - character_width:
        character_xPos = screen_width - character_width


    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    
    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_xPos
    enemy1_rect.top = enemy1_yPos

    enemy1_yPos -= enemy1_speed
    if enemy1_yPos < 0:
        enemy1_yPos = screen_height - enemy1_height
        enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
        enemy1_speed = random.randint(5, 8)
    
    
    
    
    
    
    
    
    
    
    
    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_xPos
    enemy3_rect.top = enemy3_yPos

    enemy3_yPos -= enemy3_speed
    if enemy3_yPos < 0:
        enemy3_yPos = screen_height - enemy3_height
        enemy3_xPos = random.randint(0, (screen_width - enemy3_width))
        enemy3_speed = random.randint(5, 8)


    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_xPos
    enemy2_rect.top = enemy2_yPos

    enemy2_xPos -= enemy2_speed
    if enemy2_xPos < 0:
        enemy2_yPos = random.randint(0, (screen_height - enemy2_height))
        enemy2_xPos = screen_width - enemy2_width
        enemy2_speed = random.randint(5, 8)








    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_xPos
    enemy4_rect.top = enemy4_yPos

    enemy4_xPos += enemy4_speed
    if enemy4_xPos < 0:
        enemy4_yPos = random.randint(0, (screen_height - enemy4_height))
        enemy4_xPos = screen_width - enemy4_width
        enemy4_speed = random.randint(4, 8)































    if character_rect.colliderect(enemy1_rect) or    character_rect.colliderect(enemy2_rect) or   character_rect.colliderect(enemy3_rect)  or   character_rect.colliderect(enemy4_rect):
        print("fucking shit")
        running = False







    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy1, (enemy1_xPos, enemy1_yPos))
    screen.blit(enemy2, (enemy2_xPos, enemy2_yPos))
    screen.blit(enemy3, (enemy3_xPos, enemy3_yPos))
    screen.blit(enemy4, (enemy4_xPos, enemy4_yPos))
    pygame.display.update()

pygame.quit()



