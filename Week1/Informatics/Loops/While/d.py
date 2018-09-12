import math

a = int(input())
x = 1
y = 1
while y<=a:
	x = x+(a%2)
	a = a/2
if a==1:
	print("YES")
else:
	print("NO")
