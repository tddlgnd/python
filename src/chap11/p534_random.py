# 1
import random
print(random.randint(1, 6))
print(random.randint(1, 6))

# 2
print(random.random() * 100)

# 3
myList = ["red", "green", "blue"]
print(random.choice(myList))

# 4
myList = [ [x] for x in range(10) ]
print(myList)
random.shuffle(myList)
print(myList)