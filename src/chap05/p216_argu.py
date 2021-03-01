# 1.변수를 함수의 인수로 보내면 매개변수로 복사된다.
def set_radius(radius):
    radius = 100
    return

r = 20
set_radius(r)
print(r)


# 2.리스트가 전달된다면 리스트는 원본이 직접 전달된다.
def set_radius(radius):
    radius[1]= 'a'
    return

r = [10,20,30]
set_radius(r)
print(r)
