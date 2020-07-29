################
## LISTING 36.3
################
import unittest                    #A
import funcs                       #B
 
class TestPrime(unittest.TestCase):       #C
    def test_prime_5(self):               #D
        isprime = funcs.is_prime(5)       #E
        self.assertEqual(isprime, True)   #F
    def test_prime_4(self):
        isprime = funcs.is_prime(4)
        self.assertEqual(isprime, False)
    def test_prime_10000(self):
        isprime = funcs.is_prime(10000)
        self.assertEqual(isprime, False)
        
class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = funcs.absolute_value(5)
        self.assertEqual(absolute, 5)
    def test_abs_neg5(self):
        absolute = funcs.absolute_value(-5)
        self.assertEqual(absolute, 5)
    def test_abs_0(self):
        absolute = funcs.absolute_value(0)
        self.assertEqual(absolute, 0)
        
unittest.main()  
#A unittest의 클래스와 함수를 불러옴
#B funcs.py의 클래스와 함수를 불러옴
#C 한 종류의 테스트들에 대해 하나씩 클래스를 만듦
#D 테스트. 메소드 이름이 어떤 동작을 테스트하는지 표현함
#E 5를 인자로 funcs.py에 있는 is_prime을 호출하고 결과를 isprime에 저장
#F 함수 호출 결과가 True인지 검사