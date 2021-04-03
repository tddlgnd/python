#1. 리스트 얕은 복사(shallow copy)
temps = [28, 31, 33, 35, 27, 26, 25] 
values = temps

print(temps)			# temps 리스트 출력
values[3] = 39			# values 리스트 변경
print(values)			# values 리스트가 변경되었다. 
print(temps)			# temps 리스트가 변경되었다. 
print("----")


#2. 리스트 깊은 복사(deep copy)
temps = [28, 31, 33, 35, 27, 26, 25] 
values = list(temps)

print(temps)			# temps 리스트 출력
values[3] = 39			# values 리스트 변경
print(values)			# values 리스트가 변경되었다. 
print(temps)			# temps 리스트가 변경되지 않았다. 
