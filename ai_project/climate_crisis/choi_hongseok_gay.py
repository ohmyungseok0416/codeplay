import pygame
import random

# Pygame 초기화
pygame.init()

# 창 설정
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("홍석과 태민의 여행")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 한글 폰트 설정
pygame.font.init()
font_path = pygame.font.match_font('arial')  # 한글 폰트 경로 설정
font = pygame.font.Font(font_path, 40)  # 폰트 객체 생성

# 지역과 힌트를 포함한 딕셔너리
locations = {
    "어둠의 종말": "북극: 얼음이 녹고 있는 북극은 온실 가스 배출량을 줄이는 것이 중요합니다.",
    "칠흑의 멸망": "아마존: 산불로 인한 파괴를 막기 위해 산림 보호와 재배가 필요합니다.",
    "칠흑의 종결": "태평양: 해양 생태계를 보호하기 위해 해양 청소와 재활용이 필요합니다.",
    "빛 없는 종말": "신재생 에너지: 태양, 바람, 물 등의 신재생 에너지는 환경 친화적입니다."
}

def display_text(text):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()

def game():
    running = True
    selected_location = None

    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if selected_location is None:
            text_surf, text_rect = display_text("지역을 선택해주세요! (1, 2, 3, 4 중 선택)")
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            win.blit(text_surf, text_rect)

            # 지역을 창에 표시
            y = 50
            for i, location in enumerate(locations.keys(), start=1):
                text_surf, text_rect = display_text(f"{i}. {location}")
                text_rect.center = (WIDTH // 2, y)
                win.blit(text_surf, text_rect)
                y += 50

            # 플레이어 선택 처리
            keys = pygame.key.get_pressed()
            for i, location in enumerate(locations.keys()):
                if keys[pygame.K_1 + i]:
                    selected_location = location
                    break
        else:
            hint_text = locations[selected_location]
            text_surf, text_rect = display_text(f"{selected_location}을 선택하셨습니다. 힌트: {hint_text}")
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            win.blit(text_surf, text_rect)

        pygame.display.update()

    pygame.quit()

# 게임 실행
game()
