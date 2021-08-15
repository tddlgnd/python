outfile = open("output.txt", "w", encoding="utf-8")

outfile.write("김영희\n")
print("나하나", file=outfile)

age = 20
outfile.write(f"이슬이 나이={age}\n")
outfile.write("한바위 나이=%s\n" % age)

outfile.close()