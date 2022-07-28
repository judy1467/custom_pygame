import pygame as pg
import pygame.font

pg.init() # 초기화
width, height = 600, 600
text_color = (255, 255, 255)
line_color = (255, 255, 255)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('빛의 경로')
font = pygame.font.SysFont("arial", 20, False, False)
text = font.render("times: ", True, text_color)
clock = pygame.time.Clock() #프레임 설정

# 계속 화면이 보이도록 한다.
while True:
    screen.fill((0,0,0)) # 화면 초기화
    clock.tick(30) # 30프레임
    screen.blit(text, (10, 10))
    pg.draw.rect(screen, line_color, (10, 35, 580, 555), 2) # 직사각형 그리기
    #pg.draw.line(screen, line_color, (10, 10), (100, 10), 1) # 선 긋기
    #pg.draw.lines(screen, line_color, False, ((0, 80), (50, 90), (200, 80), (220, 30)), 1) # 선 여러개 한 번에 긋기
    #pg.draw.polygon(screen, line_color, ((100, 100), (0, 200), (200, 200)), 5) # 다각형 그리기

    pg.display.update() # 화면 전체 업데이트 메소드

    for event in pg.event.get():

        if event.type == pg.QUIT: # x를 눌렀을 때 종료
            pg.quit() # pygame 종료
            exit(0) # while문 종료

# 테스트
