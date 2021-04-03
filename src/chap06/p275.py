numbers = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
sublist = numbers[2:7]
print(sublist)

print(numbers[:3])	# [10, 20, 30]

print(numbers[3:])	# [40, 50, 60, 70, 80, 90]

print(numbers[:])	# [10, 20, 30, 40, 50, 60, 70, 80, 90]

new_numbers = numbers[:]
print(new_numbers)
