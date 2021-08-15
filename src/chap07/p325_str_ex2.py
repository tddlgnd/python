# 입력한 텍스트를 문자열 분리하여 리스트로 저장한 후 세트로 변환하면 문자열 단위로 처리할 수 있다.
txt = input("입력 텍스트: ")
words = txt.split(" ")
print(words)     #분리된 문자열이 리스트로 만들어짐을 확인할 수 있다.
unique = set(words)		# 집합으로 만들면 자동적으로 중복을 제거한다. 

print("사용된 단어의 개수= ", len(unique))
print(unique)