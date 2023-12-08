import pygame

# 초기화
pygame.init()

# 화면 크기 설정
width = 1024
height = 1024
screen = pygame.display.set_mode((width, height))

# 창 제목 설정
pygame.display.set_caption("파이게임 창에 이미지와 텍스트 추가하기")

# 이미지 불러오기
image_path = "ai_project/storytelling/image/chs.png"  # 이미지 파일 경로 (이 부분을 실제 이미지 파일의 경로로 바꿔주세요)
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (width, height))  # 이미지를 화면 크기에 맞게 조절

# 폰트 설정
font = pygame.font.Font(None, 36)  # 폰트 설정 (기본 폰트, 크기 36)

# 텍스트 렌더링
text = "I am Choi Hongseok"  # 번역할 문장
text_render = font.render(text, True, (255, 255, 255))  # 텍스트를 렌더링하여 색상 설정

# 창 닫기 이벤트 처리를 위한 변수
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면에 이미지 그리기
    screen.blit(image, (0, 0))

    # 화면에 텍스트 그리기 (창 아래 중앙에 위치)
    text_rect = text_render.get_rect(center=(width // 2, height - 30))
    screen.blit(text_render, text_rect)

    # 화면 업데이트
    pygame.display.flip()

# 파이게임 종료
pygame.quit()
