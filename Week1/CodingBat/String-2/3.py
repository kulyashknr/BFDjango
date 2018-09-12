def cat_dog(str):
    cnt1 = 0
    cnt2 = 0
    for x in range (len(str)-2):
        if str[x] == 'c':
            if str[x+1]== 'a' and str[x+2]== 't':
                cnt2 = cnt2 +1
        elif str[x]== 'd':
            if str[x+1] == 'o' and str[x+2]== 'g':
                cnt1 = cnt1 +1
    if cnt1 == cnt2:
      return True
    else:
      return False
