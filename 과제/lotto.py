def make_lotto():
    setcnt = int(input("몇 세트를 만들까요? "))
    import random
    
    lotto_set = ()
    for i in range(setcnt):
        lotto = ()
        cnt = 0
        while cnt < 6:
            num = random.randint(1,45)
            if num not in lotto:
                lotto += (num, )
                cnt += 1
        lotto_set += (lotto, )
    
    i = 1
    for y in lotto_set:
        print("자동", i,  ":", end=" ")
        for z in y:
            print(z, end=" ")
        i+= 1
        print()
    
    print()        
    return lotto_set
    


        





while True:
    print("------------메뉴------------")
    print("1. 로또번호 자동 생성")
    print("2. 로또번호 당첨 확인")
    print("그외. 종료")
    print("---------------------------")
    x = input("원하는 메뉴를 선택하세요 : ")
    if x == '1':
        my_lotto_set = make_lotto()
    elif x == '2':
        check_lotto(my_lotto_set)
    else:
        break      #종료
        