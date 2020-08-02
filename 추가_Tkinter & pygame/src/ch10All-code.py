# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:32:33 2019

10장 본문의 모든 코드
@author: Kang Hwan Soo
"""
#%% 10장 1절

#%%
from tkinter import *
win = Tk()

#%% 10-01basictkwin.py	첫 tkinter 윈도 만들기 
from tkinter import *

win = Tk()
win.geometry('300x200')
win.title('반가워요, Tkinter!')
win.mainloop()

#%% 10-02widgetpack.py 레이블과 엔트리, 버튼 위젯으로 윈도 생성 
from tkinter import *

win = Tk()
win.title('여러 위젯 구성')
 
lbl = Label(win, text="레이블(Label)") #레이블
lbl.pack() #레이블을 윈도에 맞게 적정하게 배치
 
txt = Entry(win) #엔트리
txt.insert(0, '엔트리(Entry)')
txt.pack()
 
btn = Button(win, text="OK") #버튼
btn.pack()
 
win.mainloop()

#%% 10-03widgetgrid.py	테이블 형태 배치 그리드(grid) 
from tkinter import *
win = Tk()
win.title('사용자 인증')

lb1 = Label(win, text='사용자 이름')
lb2 = Label(win, text='암호')
lb1.grid(row = 0, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정
lb2.grid(row = 1, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정

et1 = Entry(win)
et2 = Entry(win)
et1.grid(row = 0, column = 1)
et2.grid(row = 1, column = 1)

#가장 하단에 버튼 2개를 저장할 레이블을 생성해 배치
lb = Label(win)
lb.grid(row=2, column=0, columnspan=2) # 두 열을 합해서 배치
bt1 = Button(lb, text='OK')
bt2 = Button(lb, text='CANCEL')
bt1.grid(row=0, column=0, padx = 10) # 외부 여백을 10을 둠
bt2.grid(row=0, column=1, padx = 10) # 외부 여백을 10을 둠
 
win.mainloop()

#%% 10-04btneventhandle.py	버튼으로 레이블의 정수 값 증가와 감소 
from tkinter import *

def add(): #1 증가시켜 레이블의 문자열에 지정
    n = int(count.get())
    n += 1
    count.set(n)

def sub(): #1 감소시켜 레이블의 문자열에 지정
    n = int(count.get())
    n -= 1
    count.set(n)

str = ['더하기', '빼기']

win = Tk()

#레이블에 표시되며, 값이 값이 쉽게 레이블에 반영될 값인 count
#tkinter가 제공하는 StringVar라는 객체에 저장
count = StringVar(value = '0') #count.set('0') 또는 value 인자에 첫 값인 0을 지정
#이후 count.get()으로 참조하고 count.set(값)으로 지정 

#키워드 인자 textvariable: 레이블에 표시할 값을 가져올 변수
#키워드 인자 textvariable에 위에서 만든 StringVar 변수인 count를 설정
data = Label(win, width = 20, textvariable = count)
data.grid(row=0, column=0, columnspan=2)

badd = Button(win, text=str[0], command = add) #누르면 함수 add() 호출
badd.grid(row=1, column=0)
bsub = Button(win, text=str[1], command = sub) #누르면 함수 sub() 호출
bsub.grid(row=1, column=1)

win.mainloop()

#%% 10-05logineventhandle.py	로그인 과정의 이벤트 처리 
from tkinter import *

users = dict(python='power', java='beauty')

def checkid():
    uid = et1.get().strip() #입력된 사용자 이름 문자열 받기
    pwd = et2.get().strip() #입력된 암호 문자열 받기
    print(uid, pwd)
    if uid in users.keys(): #사용자 이름이 있는지 검사
        if users[uid] == pwd: #사용자 이름과 암호 일치
            print('로그인 성공')
        else:
            print('암호를 확인하세요.')
    else:
        print('사용자 이름을 확인하세요.')

win = Tk()
win.title('사용자 인증')

lb1 = Label(win, text='사용자 이름')
lb2 = Label(win, text='암호')
lb1.grid(row = 0, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정
lb2.grid(row = 1, column = 0, sticky = E) #현 구역에서 위치를 오른쪽 조정

et1 = Entry(win)
et2 = Entry(win)
et1.grid(row = 0, column = 1)
et2.grid(row = 1, column = 1)

#가장 하단에 버튼 2개를 저장할 레이블을 생성해 배치
lb = Label(win)
lb.grid(row=2, column=0, columnspan=2) # 두 열을 합해서 배치
bt1 = Button(lb, text='OK', command = checkid) # 버튼을 누르면 checked 함수 호출
bt2 = Button(lb, text='CANCEL')
bt1.grid(row=0, column=0, padx = 10) # 외부 여백을 10을 둠
bt2.grid(row=0, column=1, padx = 10) # 외부 여백을 10을 둠
 
win.mainloop()

#%% 10-06convertfah.py	 버튼 이벤트 처리로 섭씨 온도를 화씨 온도로 변환
from tkinter import *

def fahrenhite(celsius):
    return celsius * 9 / 5 + 32

def clicked():
    degree = eval(cel.get()) #엔트리 cel에서 값 가져오기
    print(degree) #디버깅을 위해 출력
    fah.delete(0, END) #이전의 자료를 비우고
    fah.insert(0, str(fahrenhite(degree))) #새로 변환된 자료를 쓰고

win = Tk()
win.title('섭씨온도를 화씨온도로 변환')
 
lbcel = Label(win, text="섭씨 온도", width=10)
lbfar = Label(win, text="화씨 온도")
lbcel.grid(row=0, column=0)
lbfar.grid(row=1, column=0)

cel = Entry(win, width=20)
fah = Entry(win)
cel.grid(row=0, column=1)
fah.grid(row=1, column=1)

cvt = Button(win, text="변환", width=20, command = clicked)
cvt.grid(row=2, column=0, columnspan=2)
 
win.mainloop()

#%% 10-07canvasdrawline.py	캔버스에 직선 그리기 
from tkinter import *

win = Tk()
win.title('라인 그리기')
win.geometry('640x400+100+100')

def click(event):
    global sX, sY
    print("클릭 위치", event.x, event.y)
    sX, sY = event.x, event.y

def release(event):
    global eX, eY
    print("릴리즈 위치", event.x, event.y)
    eX, eY = event.x, event.y
    #직선 라인 그리기
    canvas.create_line(sX, sY, eX, eY, fill="blue", width=2)   

canvas = Canvas(win, relief='solid', bd=2)
canvas.pack(expand=True, fill='both')

#왼쪽 마우스 버튼 클릭 바인딩
canvas.bind("<Button-1>", click) 
#왼쪽 마우스 버튼 릴리즈 바인딩
canvas.bind("<ButtonRelease-1>", release) 

win.mainloop()

#%% 10-08imagecanvas.py	이미지 파일을 캔버스에 그리기
from tkinter import *

win = Tk()
win.title("그림 로드")
win.geometry("660x930")

#캔버스 생성
canvas = Canvas(win, bg='Yellow')
#캔버스를 윈도에 배치, 가로 세로로 확장되게
canvas.pack(expand=YES, fill=BOTH)

#사진 생성
img = PhotoImage(file="imitation.png")
#사진을 캔버스 위에 생성
canvas.create_image(10, 10, anchor=NW, image=img)

win.mainloop()

#%%	10-09imagelabel.py	이미지 파일을 레이블에 그리기	난이도: 기본
from tkinter import *

win = Tk()
win.title("레이블 그림 로드")

#사진 생성
img = PhotoImage(file="imitation.png")
#사진을 담은 레이블 생성
lbimg = Label(win, image=img)
#캔버스를 윈도에 배치, 가로 세로로 확장되게
lbimg.pack()

win.mainloop()
    
#%% 중간점검 1, 10-chk01.py 
img = PhotoImage(file="imitation.png")
canvas.create_image(10, 10, anchor=NW, image=img)

img = PhotoImage(file="imitation.png")
lbimg = Label(win, image  =img) 

#%% 중간점검 2, 09-chk02.py 
from tkinter import *
win = Tk()

btn1 = Button(win, text='left')
btn1.pack(side="left")
btn2 = Button(win, text='right')
btn2.pack(side="right", expand=True, fill='x')

win.mainloop()

#%% 10장 2절 

#%% 10-10firstpygame.py	첫 pygame 윈도 
import pygame
 
# 색상 정의
WHITE = (255, 255, 255)
# 윈도 크기 정의
size = (300, 200)
 
# 윈도 초기화
pygame.init()
 
# 화면 크기 지정해 스크린을 생성 
screen = pygame.display.set_mode(size)
#제목인 캡션 지정 
pygame.display.set_caption('첫 파이게임 윈도!')

# 윈도 종료 플래그로 사용되는 변수 초기값 지정
done = False
# 메인 루프
while not done:
    for event in pygame.event.get():  # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT:  # 윈도 종료 버튼을 누르면 
            done = True  # 프로그램 종료하기 위해 True 지정 
 
    screen.fill(WHITE) #스크린 색상을 흰색으로 지정
    pygame.display.update() # 화면의 필요한 부분만을 수정 
    #pygame.display.flip() # 화면을 전체 수정 

#메인 루프를 빠져나오면 프로그램 종료
pygame.quit()

#%% 10-11hellopygame.py	pygame 윈도에 Hello, pygame! 표시 
import pygame
 
# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
 
pygame.init()
 
# 윈도 크기 지정
size = [300, 200]
screen = pygame.display.set_mode(size)
#제목인 캡션 지정 
pygame.display.set_caption("Hello, pygame!")
  
# 폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('Arial', 20)
outstr = 'Hello, PyGame!' 
 
# 메인 루프
done = False
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
 
    screen.fill(WHITE) 
    #지정된 문자열 글씨를 그린 화면을 반환하여 text에 저장
    text = font.render(outstr, True, BLUE) 
    #글씨가 그려진 화면인 text를 윈도 스크린 위치 [x, y]에 그리기
    screen.blit(text, [100, 80])
 
    pygame.display.update()
 
pygame.quit()

#%% 10-12snownight.py	밤에 눈이 오는 모습 그리기
import pygame, random
 
# 게임 엔진 초기화
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
SIZE = [300, 300] #윈도 크기
SNOW_CNT = 70 #눈의 개수
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("눈 오는 밤")
 
# 눈의 좌표 목록 
snow_list = []
 
# snow_list에 SNOW_CNT 수만큼의 좌표를 저장
for i in range(SNOW_CNT):
    x = random.randrange(0, SIZE[0]) # x 좌표 저장
    y = random.randrange(0, SIZE[1]) # y 좌표 저장
    snow_list.append([x, y]) #목록에 추가

#화면 수정에 사용될 시계 저장 
clock = pygame.time.Clock()
 
# 메인 루프
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    # 배경색을 검은색으로
    screen.fill(BLACK)
 
    # 눈이 내리는 모습을 그리기 
    for i in range(len(snow_list)):
 
        # 눈 모양의 원을 그리기
        radius = 1
        #radius = random.randint(1, 3)
        pygame.draw.circle(screen, WHITE, snow_list[i], radius)
 
        # 눈 snow_list[i]의 y 좌표를 1 증가시켜 눈이 내리도록 수정
        snow_list[i][1] += 1
        #snow_list[i][1] += random.randint(1, 3)
        # 눈 snow_list[i]의 x 좌표를 (-1, 0, 1) 중의 하나를 선택, 이전에 값에 더하여 대입
        snow_list[i][0] += random.randint(-1, 1)
 
        # snow_list[i]가 윈도 바닥으로 넘어 내려 가면, 즉 보이지 않게 되면  
        if snow_list[i][1] > SIZE[1]: #snow_list[i][1]은 snow_list[i] 눈의 y 좌표
            # y 좌표를 위(음수)로 다시 지정
            snow_list[i][1] = random.randrange(-5, 0)
            # x 좌표도 다시 지정, snow_list[i][0]은 snow_list[i] 눈의 x 좌표
            snow_list[i][0] = random.randrange(0, SIZE[0])
 
    pygame.display.update()
    #초당 수정될 프레임 수 지정, 초당 20 프레임 화면이 수정됨  
    clock.tick(20)
 
pygame.quit()    

#%% 중간점검 3, 09-chk03.py 
# 폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('Arial', 20)
outstr = 'Hello, PyGame!' 
... 
while not done:
	... 
    text = font.render(outstr, True, BLUE) 
    #글씨가 그려진 화면인 text를 윈도 스크린 위치 [x, y]에 그리기
    screen.blit(text, [100, 80])

#%% 중간점검 4, 09-chk04.py 
#pip install pygame

#%% 프로젝트 Lab 10-pl01-movebutton.py	마우스를 도망가는 버튼 
from random import randrange
from tkinter import *

#버튼에 마우스가 들어오면 버튼 위치를 이동시키는 함수
def escapemouse(e):
    #윈도 전체 크기 저장
    w = win.winfo_width()
    h = win.winfo_height()
    print('원도 크기: ', w, h)
    #버튼 크기 저장
    bw = btn.winfo_width()
    bh = btn.winfo_height()
    print('버튼 크기: ', bw, bh)
    #난수로 그려질 버튼이 보이도록 위치 (rx, ry) 지정
    rx = randrange(0, w - bw)
    ry = randrange(0, h - bh)
    #위치로 버튼 이동 
    print('이동 위치: ', rx, ry)
    btn.place(x=rx, y=ry)

win = Tk()
win.geometry("600x300+100+100")
win.title('마우스를 도망가는 버튼')
win.resizable(False, False)

btn = Button(win, text='저를 눌러 보세요!', command=win.quit)
#버튼의 첫 위치 지정
btn.place(x=200, y=30)
#btn.place(relx=0.5, rely=0.5)

#마우스가 버튼 위로 들어오면 함수 escapemouse가 실행되도록 연결
btn.bind('<Enter>', escapemouse)

win.mainloop()

#%% 프로젝트 Lab 10-pl02-moverectangle.py	화살표 키보드로 사각형 이동
import pygame
from pygame.locals import QUIT, KEYUP, KEYDOWN, \
                 K_LEFT, K_RIGHT, K_UP, K_DOWN
 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#화면에 사각형 그리고 초당 화면 프레임 수정
def paint(surface, x, y):
    #사각형 그리기
    def drawrect(surface, x, y):
        sizeX, sizeY = 30, 30 
        pygame.draw.rect(surface, GREEN, [x, y, sizeX, sizeY])

    surface.fill(WHITE)
    drawrect(surface, x, y)
    pygame.display.update()
    #초당 화면 수정 프레임 수 지정
    clock.tick(60)

#시작: 초기화 
pygame.init()
surface = pygame.display.set_mode([600, 400])
pygame.display.set_caption("키보드 이벤트 처리")
 
#화면 수정 시간에 사용
clock = pygame.time.Clock()
 
# 방향키에 따른 이동 거리와 첨자 관리
INC = (-2, 0, 2) #방향 키에 따른 이동 거리
posX = 1 #위 값 중의 하나 첨자
posY = 1 #위 값 중의 하나 첨자
# 사각형의 첫 위치
x, y = 10, 10

#메인 루프 
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
 
        # 키를 누르면
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_LEFT:
                posX = 0
            elif key == K_RIGHT:
                posX = 2
            elif key == K_UP:
                posY = 0
            elif key == K_DOWN:
                posY = 2
 
        # 키를 올리면(놓으면)
        elif event.type == KEYUP:
            key = event.key
            # 왼쪽 오른쪽 키면, x 증가를 0으로 
            if key == K_LEFT or key == K_RIGHT:
                posX = 1
            # 위 아래 키면, y 증가를 0으로 
            elif key == K_UP or key == K_DOWN:
                posY = 1
                
    #좌표 (x, y)를 수정해 사각형 그리기
    x, y = x + INC[posX], y + INC[posY]
    paint(surface, x, y)
  
pygame.quit()

#%% EOF 종료 

