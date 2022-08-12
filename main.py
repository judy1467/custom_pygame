import pygame as pg
import pygame.font

pg.init() # 초기화

width, height = 600, 600
default_color = (255, 255, 255)
screen = pg.display.set_mode((width, height))
pg.display.set_caption('빛의 경로')
font = pygame.font.SysFont("arial", 20, False, False)
text = font.render("times: ", True, default_color)
clock = pygame.time.Clock() #프레임 설정
arrow = pygame.image.load("resources/images/arrow.png")
map = pygame.image.load("resources/convert/map1.jpg")
bg_rect = (10, 35, 580, 555) # width = 570, height = 520
keys = [False, False, False, False]
playerpos = [100, 100]

while True:
    screen.fill((0,0,0)) # 화면 초기화
    clock.tick(60) # 60프레임
    pg.draw.rect(screen, default_color, bg_rect, 2) # 직사각형 그리기
    screen.blit(map, (10+2, 35+2))
    screen.blit(arrow, playerpos)
    screen.blit(text, (10, 10))

    pg.display.update() # 화면 전체 업데이트 메소드

    #pg.draw.line(screen, , (10, 10), (100, 10), 1) # 선 긋기
    #pg.draw.aaline(screen, , (10, 10), (100, 10), True) # 부드러운 선 긋기
    # 부드러운 선 은 두께가 1로 고정
    #pg.draw.aalines(screen, default_color, False, ((0, 80), (50, 90), (200, 80), (220, 30)), 1) # 선 여러개 한 번에 긋기
    #pg.draw.polygon(screen, default_color, ((100, 100), (0, 200), (200, 200)), 5) # 다각형 그리기

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # pygame 종료
            exit(0) # while문 종료
        if event.type == pg.KEYDOWN: # 키다운 감지
            if event.key == pg.K_UP:
                keys[0] = True
            elif event.key == pg.K_LEFT:
                keys[1] = True
            elif event.key == pg.K_DOWN:
                keys[2] = True
            elif event.key == pg.K_RIGHT:
                keys[3] = True
        if event.type == pg.KEYUP: # 키업 감지
            if event.key == pg.K_UP:
                keys[0] = False
            elif event.key == pg.K_LEFT:
                keys[1] = False
            elif event.key == pg.K_DOWN:
                keys[2] = False
            elif event.key == pg.K_RIGHT:
                keys[3] = False

    if keys[0]: # 화살표 이동
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    if keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5

    if playerpos[0] < bg_rect[0]: # 화살표 이동범위 제한
        playerpos[0] = bg_rect[0]
    elif playerpos[0] > bg_rect[2]:
        playerpos[0] = bg_rect[2]
    if playerpos[1] < bg_rect[1]:
        playerpos[1] = bg_rect[1]
    elif playerpos[1] > bg_rect[3]:
        playerpos[1] = bg_rect[3]
