##
# 이 프로그램은 피보나치 수열을 반환하는 이터레이터 객체를 정의한다.
#
class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue
        
    def __iter__(self):
        return self
    
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b
        self.b = n
        return n
    
for i in FibIterator():
    print(i, end=" ")
