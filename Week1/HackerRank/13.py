def swap_case(s):
    str = ""
    for x in s:
        if x.isupper(): 
            str = str + x.lower()
        else: 
            str = str + x.upper()
    return str
