str = input()
l = list(str)
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
for i in range(len(l)):
    if l[i].isalnum():
        cnt1 = cnt1 +1
    if l[i].isalpha():
        cnt2 = cnt2 +1
    if l[i].isdigit():
        cnt3 = cnt3 +1
    if l[i].islower():
        cnt4 += 1
    if l[i].isupper():
        cnt5 += 1
if cnt1 > 0:
    print("True")
else:
    print("False")
if cnt2 > 0:
    print("True")
else:
    print("False")
if cnt3 > 0:
    print("True")
else:
    print("False")
if cnt4 > 0:
    print("True")
else:
    print("False")
if cnt5 > 0:
    print("True")
else:
    print("False")
