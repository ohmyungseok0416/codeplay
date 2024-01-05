import pygame

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
font = pygame.font.Font(font_path, 30)  # 폰트 객체 생성

# 스토리와 선택지
story = [
    "태민은 환경변화로 빠르게 녹고 있는 북극에 도착했습니다. 얼음이 녹고 있는 모습을 보며 온실 가스 배출이 지구에 미치는 영향에 대해 깨달았습니다.",
    "1. 극지방 도착",
    "2. 산란기 지원 도착",
    "3. 생존을 위한 자원 수집",
    "4. 어린 아이와의 만남",
    "5. 자원 부족과 갈등",
    "6. 구조를 위한 노력",
    "7. 결말"
]

# 선택지
choices = [
    ("1. 극지방 도착", "2. 산란기 지원 도착"),
    ("3. 생존을 위한 자원 수집", "4. 어린 아이와의 만남"),
    ("5. 자원 부족과 갈등", "6. 구조를 위한 노력"),
    ("7. 결말", "8. 끝내기")
]

def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

def main():
    running = True
    current_stage = 0

    while running:
        win.fill(WHITE)
        display_text(story[current_stage], 50, 50)

        choice1, choice2 = choices[current_stage]
        display_text(choice1, 300, 0)
        display_text(choice2, -300, 0)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_stage += 1
                    if current_stage >= len(story):
                        current_stage = len(story) - 1
                elif event.key == pygame.K_2:
                    current_stage += 2
                    if current_stage >= len(story):
                        current_stage = len(story) - 1

    pygame.quit()

if __name__ == "__main__":
    main()