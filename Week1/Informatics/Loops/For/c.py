import math
a = int(input())
b = int(input())

for x in range(a,b+1):
	i = int(math.sqrt(x))
	if i*i==x:
		print(x,end=" ")
