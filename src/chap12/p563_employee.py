class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def  getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus =bonus

    def  getSalary(self):       #메서드 오버라이드
        salary = super().getSalary()
        return salary + self.bonus

    def __str__(self):          #연산자 재정의(오버로딩)
        return "이름: "+ self.name+ "; 월급: "+ str(self.salary)+\
               "; 보너스: "+str(self.bonus)

kim = Manager("김철수", 2000000, 1000000)

print(kim)

print(f"총 급여 : {kim.getSalary()}원")