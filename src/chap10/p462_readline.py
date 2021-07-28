infile = open("input.txt", "r", encoding="utf-8")
line = infile.readline()
# line = infile.readline().rstrip()  #줄바꿈 문자(\n)를 삭제하여 빈 줄 출력을 제거
while line != "" :
	print(line)
	line = infile.readline()
    # line = infile.readline().rstrip()