import math
def xor(x,y):
    if x==y:
    	return 0
    else:
    	return 1

l = []
for x in range(1):
    l = list(input().split(" "))
x = int(l[0])
y = int(l[1])
print(xor(x,y))
