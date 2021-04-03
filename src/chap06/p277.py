lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']    # 리스트 일부(0에서 2번째) 변경
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]     # 99를 중간에 추가
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = []    # 리스트의 모드 요소를 삭제
print(lst)

numbers = list(range(0,10))
del numbers[-1]    # 마지막 항목 삭제
print(numbers)

numbers = list(range(0,10))
del numbers[0:2]   # 0에서 1번째 까지 삭제
print(numbers)

numbers = list(range(0,10))
del numbers[:]   # 전체를 삭제
print(numbers)