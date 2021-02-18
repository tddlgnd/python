# 1 올바른 조건 순서
score = 72

if score >= 90 :
	print("학점 A")
elif score >= 80 :
	print("학점 B")
elif score >= 70 :
	print("학점 C")
elif score >= 60 :
	print("학점 D")
else :
	print("학점 F")
print("---")


# 2 잘못된 조건 순서
score = 72

if score >= 60 :
	print("학점 D")
elif score >= 70 :
	print("학점 C")
elif score >= 80 :
	print("학점 B")
elif score >= 90 :
	print("학점 A")
else :
	print("학점 F")
print("---")    
  
  
# 3 독립적인 if을 여러개 사용
score = 72

if score >= 90 :
	print("학점 A")
if score >= 80 :
	print("학점 B")
if score >= 70 :
	print("학점 C")
if score >= 60 :
	print("학점 D")
if score < 60 :
	print("학점 F")
print("---")