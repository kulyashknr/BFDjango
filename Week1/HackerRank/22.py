def minion_game(string):
    kev = 0
    stu = 0
    for i in range(len(string)):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            kev= kev + len(string)-i 
        else:
            stu = stu + len(string)-i 
    if  kev>stu: 
        print("Kevin", kev) 
    elif kev == stu:
        print("Draw")
    else:
        print("Stuart", stu)
