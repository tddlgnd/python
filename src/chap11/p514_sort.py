# 1. Class 사용하는 경우
class Student:
        def __init__(self, name, grade, number):
                self.name = name
                self.grade = grade
                self.number = number
        def __repr__(self):
                return repr((self.name, self.grade, self.number))

students = [
        Student('홍길동', 3.9, 20160303),
        Student('김철수', 3.0, 20160302),
        Student('최자영', 4.3, 20160301),
]
print(students)
print(sorted(students, key=lambda student: student.number))
print(sorted(students, key=lambda student: student.number, reverse=True))


# 2. Class를 사용하지 않는다면 다음처럼 코딩
students = [
        ('홍길동', 3.9, 20160303),
        ('김철수', 3.0, 20160302),
        ('최자영', 4.3, 20160301),
]
print(sorted(students, key=lambda student: student[2]))
print(sorted(students, key=lambda student: student[2], reverse=True))