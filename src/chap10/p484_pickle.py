#1 pickle 모듈을 이용하여 파일로 저장하기
import pickle

gameOption = { 			# 파일을 닫는다.	
			 "Sound": 8,
			 "VideoQuality": "HIGH",
			 "Money": 100000,
			 "WeaponList": ["gun", "missile", "knife" ]
}

file = open("save.p", "wb")	# 이진 파일 오픈
pickle.dump(gameOption, file)	# 딕셔너리를 피클 파일에 저장
file.close()				# 파일을 닫는다.




#2 pickle 모듈을 이용하여 파일로 저장된 딕셔너리 읽기
import pickle

file = open("save.p", "rb")		# 이진 파일 오픈
obj = pickle.load(open("save.p", "rb"))	# 피클 파일에 딕션너리를 로딩
print(obj)