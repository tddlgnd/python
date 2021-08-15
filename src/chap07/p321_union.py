A ={"apple","banana","grape"}
B ={"apple","banana","kiwi"}

# 합집합
C = A | B    #또는 C = A.union(B)
print(C)


# 교집합
C = A & B    #또는 C = A.intersection(B)
print(C)


# 차집합
C = A - B    #또는 C = A.diffenrence(B)
print(C)