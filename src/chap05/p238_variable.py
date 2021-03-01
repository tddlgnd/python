# 1. 지역변수
def myfunc():
  x = 100
  print(x)

myfunc()
# print(x)


# 2. 전역변수
gx = 100

def myfunc():
  print(gx)

myfunc()
print(gx)


# 3. 지역변수는 함수마다 동일한 이름을 사용할 수 있다.
def myfunc() :
    x = 200
    print(x)

def main() :
    x = 100
    print(x)

myfunc()
main()


# 4. 함수 안에서 전역변수 변경하기
gx = 100

def myfunc() :
    gx = 200    #전역변수를 함수 안에서 변경하면 지역변수로 새로 만들어진다.
    print(gx)

myfunc()
print(gx)

