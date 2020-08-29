'''
1. 
다음과 같은 기능을 가지는 Counter 클래스를 정의하고 인스턴스를 구현하자.

이 클래스는 __number라는 속성 값을 가짐.
number를 매개 변수로 가지는 __init__(self, number) 메소드를 가짐. number의 디폴트 매개변수 값은 0임. number가 100 이상이 되거나 -1 이하가 되면 0 값을 초기 값으로 가짐.
number를 0으로 초기화 하는 reset() 메소드를 가짐.
__number를 1 증가시키는 inc() 메소드를 가짐, __number가 100 이상이 되면 0으로 초기화 됨.
__number를 1 감소시키는 dec() 메소드를 가짐, __number가 -1 이하가 되면 0 값을 가짐.
C(n)과 같이 n을 출력하는 __str__() 특수 메소드를 가짐.
이 인스턴스를 사용하는 다음 코드를 작성하고 그 결과를 분석해보자.

c1 = Counter(10)
c1.inc()
print('c1 =', c1)
c2 = Counter()
c2.inc()
c2.inc()
c2.dec()
print('c2 =', c2)
c2.reset()
print('c2 =', c2)
'''

class Counter:
  def __init__(self, number=0):
    self.number = number
    
  def reset(self):
    self.number = 0
    
  def inc(self):
    self.number = self.number + 1
    if self.number >= 100:
      self.number = 0
    
  def dec(self):
    self.number = self.number - 1
    if self.number <= -1:
      self.number = 0

  def __str__(self):
    return 'C({})'.format(self.number)
    
c1 = Counter(10)
c1.inc()
print('c1 =', c1)

c2 = Counter()
c2.inc()
c2.inc()
c2.dec()
print('c2 =', c2)
c2.reset()
print('c2 =', c2)


'''
2. 다음과 같은 기능을 가지는 은행계좌 클래스 BankAccount 클래스를 구현하여라. 그리고 이 클래스를 이용하여 인스턴스를 생성하여라. 이 클래스는 다음과 같은 속성과 동작을 가진다.

속성
이름(name)
계좌번호(account_num)
잔액(balance)

메서드
예금 기능 : deposit(money) - money 만큼의 돈을 balance에 추가한다.
출금 기능 : withdraw(money) - money 만큼의 돈이 balance에서 빠져나간다(balance가 money보다 작으면 출금이 되지 않는다).

BankAccount라는 클래스를 만든 후 다음과 같이 account1이라는 계좌를 생성하고 2000원을 입금하여라. 이 계좌 정보를 출력한 후 500원을 출금한 후 다음과 같이 계좌 정보를 출력하여라. 마지막으로 5000원을 출금하여라.

account1 = BankAccount("홍길동", "1234-0001")
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)

실행 결과
홍길동님의 계좌 1234-0001의 잔고는 0원입니다.
2000원이 입금되었습니다. 잔고는 2000원입니다.
홍길동님의 계좌 1234-0001의 잔고는 2,000원입니다.
홍길동님의 계좌 1234-0001의 잔고는 1,500원입니다.
계좌 잔고는 1500원으로 인출 요구 금액 5000원보다 작습니다.
'''
class BankAccount:
    def __init__(self, name, account_num, balance=0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    
    def get_balance():
      return self.balance
    
    def deposit(self, money):
        self.balance += money
        print(money, '원이 입금되었습니다. 잔고는 ', self.balance, '원입니다.')
        return self.balance
  
    def withdraw(self, money):
        if self.balance - money > 0 :
            self.balance -= money
        else:
            print('계좌 잔고는 ', self.balance, '원으로 인출 요구 금액 ', money, '원보다 작습니다.')

    def __str__(self):
      return str(self.name) + '님의 계좌 ' + str(self.account_num) + '의 잔고는 ' + str(self.balance) +'원입니다.'
      
account1 = BankAccount("홍길동", "1234-0001")
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)      