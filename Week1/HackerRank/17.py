def count_substring(string, sub_string):
    cnt = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            r = i+len(sub_string)
            if string[i:r] == sub_string:
                cnt=cnt+1

    return cnt
