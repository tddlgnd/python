import random
myList = [ "앞면", "뒷면" ]

while (True):
	response = input("동전 던지기를 계속하시겠습니까?(y, n) ");
	if response == "y":
		coin = random.choice(myList)
		print(coin)
	else :
		break