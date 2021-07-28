#1 대소문자 변환하기 
s = "i am a student."
print(s.capitalize())   # 첫글자만 대문자로
print(s.lower())    # 모두 소문자로
print(s.upper())    # 모두 대문자로


#2 찾기 및 바꾸기
s = input("파이썬 소스 파일 이름을 입력하시오: ")
if s.endswith(".py"):
	print("올바른 파일 이름입니다")
else :
	print("올바른 파일 이름이 아닙니다.")

    
s = "www.naver.com"
print(s.replace("com", "co.kr"))


s = "www.naver.co.kr"
print(s.find(".kr"))


s = "Let it be, let it be, let it be"
print(s.rfind("let"))


s = "www.naver.co.kr"
print(s.count("."))
print(s.count(".", 0, 5))


#3 문자 분류
print("ABCabc".isalpha())
print("영이공".isalpha())
print("123".isdigit())
print("abc".islower())


#4 공백문자 제거
s = " Hello, World! "
print(s.strip())

s = "########this is example#####"
print(s.strip("#"))

s = "########this is example#####"
print(s.lstrip("#"))
print(s.rstrip("#"))


#5 문자열을 분리하기
s = "Welcome to Python"
print(s.split())

s = "Hello, World!"
print(s.split(","))

s = "Hello, World!"
print(s.split(", "))

print(list("Hello, World!"))  #문자열을 리스트로 변환하면 문자로 따로따로 분리


#6 문자열 결합하기
print(",".join(["apple", "grape", "banana"]))

print("-".join("010.1234.5678".split(".")))

s = "hello world" 
clist = list(s)
print(clist)
"".join(clist)  #문자들을 다시 문자열로 만들 때도 사용







