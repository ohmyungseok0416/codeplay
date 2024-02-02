# -*- coding: utf-8 -*-

import pygame
import sys

pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("태민의 여정")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 한글 폰트 설정
pygame.font.init()
font_path = pygame.font.match_font('malgun Gothic')  # 맑은 고딕 폰트 경로 설정
font = pygame.font.Font(font_path, 20)  # 폰트 객체 생성

# 스토리와 선택지
story = [
    ("1. 극지방 도착", "태민은 얼음이 녹고 있는 북극으로 도착했지만, 갑작스러운 기후 변화로 인해 머물기 어려운 상황에 처합니다. 어디로 이동하시겠습니까?"),
    ("1: 남쪽으로 이동하기", "2: 북쪽으로 이동하기"),
    ("2. 연구기지 도착", "남쪽으로 간 태민은 주변에서 연구기지을 발견합니다. 하지만 연구기지 또한 온실가스의 영향으로 연구기지 쪽 얼음이 녹고있었습니다. 연구기지에서 생존한 최홍석이 도움을 요청합니다. 최홍석은 6수를 한 파렴치한 부모님 등골브레이커지만, 끝내 배재대학교에 입학한 개상노무새끼입니다. 어떤 도움을 주시겠습니까?"),
    ("1: 가지고 있는 식량 나눠주기", "2: 무시하기"),
    ("3. 생존을 위한 자원 수집", "식량을 나눠준 태민은 연구기지 연구원의 호감을 샀습니다. 그리고 함께 생존을 위한 자원을 찾아 다니며, 음식과 보온 재료, 그리고 위생 용품을 수집합니다. 하지만 태민은 이러한 자원이 점점 부족해지고 있음을 알게 됩니다. 어떻게 할 것인가요?"),
    ("1: 최홍석과 결별하기", "2: 최홍석과 끝까지 함께 가기"),
    ("4. 천재 물리학자 오명석과의 만남", "연구원들과 헤어진 태민은 또 다른 연구기지를 발견하게 됩니다. 그곳엔 식량이 충분히 있었고 모아뒀던 전기도 충분히 있는 것 같습니다. 또한 연구기지엔 천재 물리학자 오명석이 있었습니다. 오명석은 18살에 고등학교의 전 과목을 마스터하고 졸업해 서울대학교 물리학과에서 2년만에 박사학위로 졸업을 한 대한민국 최고의 인적자원이자 오인슈타인으로 불리워지는 인물이였습니다. 명석이 태민을 킬러로 오해하고 죽이려합니다. 어떤 말로 명석을 설득시키시겠습니까?"),
    ("1: 식량을 보여준다.", "2: 노예가 되겠다고 한다."),
    ("5. 자원 부족과 갈등", "명석의 노예가 된 태민은 연구기지에 있는 자원을 닥치는대로 쓰고있습니다. 그러한 태민의 태도에 분노한 명석과 태민 간에 자원 부족으로 인한 갈등이 시작됩니다. 태민은 이를 조절하고자 하지만, 상황은 점점 악화되고 있습니다. 어떻게 해결하시겠습니까?"),
    ("1: 나가서 자원 구해오기", "2: 자원을 챙겨서 이동하기."),
    ("6. 구조를 위한 노력", "연구기지를 떠난 태민과 명석은 탐사선을 찾았습니다. 비록 얼음이 녹아내려 바다에 떠있어서  작동은 하지 않겠지만 구조요청은 보낼 수 있을겁니다.  태민은 명석과 함께 구조를 위한 신호를 보내려고 합니다. 바다에 떠있는 탐사선까지 어떻게 가실겁니까?"),
    ("1: 태민이 수영해서 구조신호를 보낸다.", "2: 명석이 수영해서 구조신호를 보낸다."),
    ("7. 결말", "다행히 수영을 할 줄 알던 태민이 탐사선까지 도착 해서 구조신호를 보냈습니다. 곧이어 구조선이 오고, 태민은 어려운 여정 끝에 구조되어 생존을 이끌어냅니다. 그는 자신의 경험을 통해 온실 가스 배출과 환경 파괴로 인한 위험성을 알리고자 합니다. 이를 통해 태민은 지구 환경 보호의 중요성을 널리 알립니다."),
]

def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(left=x, top=y)
    win.blit(text_surface, text_rect)

def display_choices(choice1, choice2):
    text_surface1 = font.render(choice1, True, BLACK)
    text_rect1 = text_surface1.get_rect(center=(WIDTH // 4, HEIGHT - 50))
    win.blit(text_surface1, text_rect1)

    text_surface2 = font.render(choice2, True, BLACK)
    text_rect2 = text_surface2.get_rect(center=(WIDTH * 3 // 4, HEIGHT - 50))
    win.blit(text_surface2, text_rect2)

def main():
    running = True
    current_stage = 0

    while running:
        win.fill(WHITE)

        # 제목
        display_text(story[current_stage][0], 20, 20)

        # 이야기
        if len(story[current_stage][1]) > 20:
            display_text(story[current_stage][1][:20], 20, 70)
            display_text(story[current_stage][1][20:], 20, 90)
        else:
            display_text(story[current_stage][1], 20, 70)

        # 선택지 표시
        if current_stage < len(story) - 1:
            display_choices(story[current_stage + 1][0], story[current_stage + 1][1])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_stage += 1
                elif event.key == pygame.K_2:
                    current_stage += 2  # 선택지 2번 선택 시 다다음 스테이지로 이동하도록 수정

                if current_stage >= len(story) - 1:
                    current_stage = len(story) - 1

    pygame.quit()

if __name__ == "__main__":
    main()
