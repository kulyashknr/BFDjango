import math
def powerr(a, n):
    return pow(a,n)

l = []
for x in range(1):
    l = list(input().split(" "))
a = float(l[0])
n = int(l[1])
if n>= 0:
	print(powerr(a,n))
