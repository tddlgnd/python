#1 가격이 저장된 리스트가 있는 경우, 가격이 음수이면 0으로 바꾸는 코드
prices = [135, -545, 922, 356, -992, 217]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)


#2 단어의 첫글자만을 추출하여 리스트로 만드는 코드
words = ["All", "good", "things", "must", "come", "to", "an", "end."]
letters = [ w[0] for w in words ]
print(letters)


#3 x와 y 인수를 동시에 사용하여 리스트 함축
numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers)
