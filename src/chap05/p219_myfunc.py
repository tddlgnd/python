def myfunc(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(myfunc(a="Hi!", b="Mr.", c="Kim"))
#print(myfunc(a="오늘의 ", b="날씨는 ", c="최고 20도, ", d="최저 12도 ", e="입니다"))
