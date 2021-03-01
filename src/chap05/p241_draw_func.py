##
#	이 프로그램은 터틀 그래픽으로 함수를 그린다. 
#
import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)      # x, y 좌표 그리기
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
	t.goto(x, int(0.01*f(x)))      #기울기를 완만하게 하기 위해 0.01을 곱한다.

turtle.mainloop()
turtle.bye()	
