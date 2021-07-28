#1 map() 함수와 람다식
list_a = [ 1, 2, 3, 4, 5 ]
f = lambda x : 2*x
result = map(f, list_a)
print(list(result))


#2 filter() 함수와 람다식
list_a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x : x % 2 == 0, list_a) 
print(list(result))


data = [(3, 100), (1, 200), (7, 300), (6, 400)]
print(sorted(data, key=lambda item: item[0]))


#3 reduce() 함수와 람다식
import functools
result = functools.reduce(lambda x,y: x+y, [1, 2, 3, 4])
print(result)