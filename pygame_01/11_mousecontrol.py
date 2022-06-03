# -*- coding: utf-8 -*-

import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("fucking mousecontrol")


character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height










circleX_pos = 0
circleY_pos = 0





clock = pygame.time.Clock()

running = True
while running:      
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # print("mouseMotion")
            # print(pygame.mouse.get_pos()) #마우스 움직이는 위치 좌표 출력
            character_xPos, character_yPos = pygame.mouse.get_pos()
            # screen.fill((0, 0, 0))
            # pygame.draw.circle(screen, (255, 0, 255),  (circleX_pos , circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouseButtonDOWN")
            print(pygame.mouse.get_pos())
            print(event.botton) # 마우스에서 눌리는 버튼의 종류 화면에 출력(어떤거 눌렀는지)

            if event.button == 1:
                print("좌클")
            elif event.button == 3:
                print("우클")
            elif event.button == 2:
                print("휠 클")
            elif event.button == 4:
                print("휠 업")
            elif event.button == 5:
                print("휠 다운")


        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseButtonUp")
            pass

    screen.fill((11, 55, 26))
    screen.blit(character, (character_xPos, character_yPos))

    # 3, 게임 캐릭터 위치 정의

    # 4, 충돌처리

    #5, 화면에 그리기
    pygame.display.update() # 게임화면을 새로고침해줌.

    #종료시간 살짝 늦추기
    # pygame.time.delay(2000)

    #종료처리
pygame.quit()         