#1 read() 사용
infile = open("input.txt", "r", encoding="utf-8")
s = infile.read()
print(s)
infile.close()


#2 readline() 사용
infile = open("input.txt", "r", encoding="utf-8")
lines = infile.readlines()
for line in lines :
	print(line)
infile.close()