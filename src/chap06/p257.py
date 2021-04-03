#1
temps =[28,31,33,35,27,26,25] 

for i in range(len(temps)):
	print(temps[i], end=', ')

#2
temps =[28,31,33,35,27,26,25] 

for element in temps:
	print(element, end=', ')

#3
questions =['name','quest','color']
answers =['Kim','파이썬','blue']
for q, a in zip(questions, answers):
	print(f"What is your {q}?  It is {a}")
