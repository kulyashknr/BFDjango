def count_hi(str):
    cnt = 0
    for x in range (len(str)-1):
        if str[x]== 'h' and str[x+1]== 'i':
            cnt = cnt + 1
    return cnt
