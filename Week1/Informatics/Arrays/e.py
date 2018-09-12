n = int(input())
l = []
i = 0
for x in range(1):
	l = list(input().split(" "))
for x in range(0,len(l)-1):
	if int(l[x])*int(l[x+1])>0:
		print("YES")
		break
else:
	print("NO")
