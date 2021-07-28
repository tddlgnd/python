#1 직접 코딩
text_data ="Create the highest, grandest vision possible for your life, because you become what you believe"
# text_data = "오늘 옷차림을 가볍게 했는데도 땀이 날 정도로 날이 덥습니다. 오늘 낮 기온 어제보다 확실히 오르는 속도가 빠르겠습니다. 오늘 최고 기온 서울은 29도, 대전과 광주는 30도까지 높아질 것으로 예상되는데요"

word_dic = {}				# 단어들과 출현 횟수를 저장하는 딕셔너리를 생성
for w in text_data.split():		# 텍스트를 단어들로 분리하여 반복한다. 
     if w in word_dic:			# 단어가 이미 딕셔너리에 있으면
         word_dic[w]  += 1  		# 출현 횟수를 1 증가한다. 
     else:				# 처음 나온 단어이면 1로 초기화한다. 
         word_dic[w]   = 1  

for w, count in sorted(word_dic.items()):	# 키와 값을 정렬하여 반복 처리한다. 
     print(w, "의 등장횟수=", count)
     

#2 이미 구현된 클래스 Counter 사용 – 분석결과는 딕셔너리로 생성
from collections import Counter
text_data ="Create the highest, grandest vision possible for your life, because you become what you believe"
# text_data = "오늘 옷차림을 가볍게 했는데도 땀이 날 정도로 날이 덥습니다. 오늘 낮 기온 어제보다 확실히 오르는 속도가 빠르겠습니다. 오늘 최고 기온 서울은 29도, 대전과 광주는 30도까지 높아질 것으로 예상되는데요"

a = Counter(text_data.split())

print(a) 
