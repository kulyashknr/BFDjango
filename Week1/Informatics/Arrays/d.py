n = int(input())
l = []
i = 0x
for x in range(1):
    l = list(input().split(" "))
for x in range(1,len(l)):
    if int(l[x])>int(l[x-1]):
    	i = i+1
print(i)
