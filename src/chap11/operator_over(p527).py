##
#	이 프로그램은 연산자 중복을 사용하여 Book 객체의 len() 연산을 구현한다. 
#
class Book:
	title = ''
	pages = 0

	def __init__(self, title='', pages=0):
		self.title = title
		self.pages = pages

	def __str__(self):
		return self.title

	def __gt__(self, other):
		return self.pages > other.pages

book1 = Book('test1', 600)
book2 = Book('test2', 500)
if book1 > book2 :
	print(book1)
else:
	print(book2)
# print(book1 > book2)