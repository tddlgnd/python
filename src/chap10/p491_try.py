#1  예외처리
(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError:
    print("0으로 나누는 예외")


#2  시스템이 내보내는 예외 메시지를 출력
(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError as e:
    print(e)
    
   
#3  정수를 받아야 하는데 다른 수를 입력한 예외처리
while True:
    try:
        n = input("숫자를 입력하시오 :  ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오. ")
print("정수 입력이 성공하였습니다!")


#4  파일 오류를 처리하는 예외처리
try:
    fname = input("파일 이름을 입력하세요: ")
    infile = open(fname, "r") 
except IOError:
    print("파일 " + fname + "을 발견할 수 없습니다.")