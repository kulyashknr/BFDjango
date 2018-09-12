import math

a = int(input())
i = 1
while i < math.sqrt(a):
    print(i*i)
    i = i +1
if math.sqrt(a)*math.sqrt(a) == a:
    print(a)
