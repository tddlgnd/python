#가위, 바위, 보 게임
import random

human = int(input("선택하시오 (1: 가위, 2: 바위, 3: 보) "))
computer = random.randint(1, 3)

if human == computer :
    result = "비김"
elif human == 1 and computer == 2 :
    result = "컴퓨터 승"
elif human == 1 and computer == 3 :
    result = "사람 승"
elif human == 2 and computer == 3 :
    result = "컴퓨터 승"
elif human == 2 and computer == 1 :
    result = "사람 승"
elif human == 3 and computer == 1 :
    result = "컴퓨터 승"
else :
    result = "사람 승"
    
print(result)
print(computer)




