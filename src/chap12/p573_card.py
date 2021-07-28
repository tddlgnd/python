##
#	클래스 간의 HAS-A 관계를 구현한다. 
#
class Card:
    suitNames = ['클럽', '다이아몬드', '하트', '스페이드']
    rankNames = [None, '에이스', '2', '3', '4', '5', '6', '7', '8', '9', '10', '잭', '퀸', '킹']
    
    #생성자로 카드 1장을 나타내는 객체를 초기화한다.
    #suit는 카드의 무늬, rank는 카드의 숫자이다.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #카드 1장을 문자열로 나타낸다. 
    #리스트를 사용하여 카드의 숫자를 문자열로 변환한다.
    def __str__(self):
        return Card.suitNames[self.suit]+" "+\
                             Card.rankNames[self.rank]

class Deck:
    #cards 리스트에 Card 객체를 생성하여 추가한다.
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)     #has-a 관계 
                self.cards.append(card)
                
    #cards 리스트에 있는 Card 객체의 문자열 표현을 얻어서 리스트를 만든 후 출력한다.
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()		# 덱 객체를 생성한다. 
print(deck)		# 덱 객체를 출력한다. __str__()이 호출된다. 