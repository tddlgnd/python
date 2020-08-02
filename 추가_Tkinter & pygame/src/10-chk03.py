
# 폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('Arial', 20)
outstr = 'Hello, PyGame!' 
... 
while not done:
	... 
    text = font.render(outstr, True, BLUE) 
    #글씨가 그려진 화면인 text를 윈도 스크린 위치 [x, y]에 그리기
    screen.blit(text, [100, 80])