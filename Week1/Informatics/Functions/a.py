def mini(a, b, c, d):
    return (min(a,min(b,min(c,d))))

l = []
for x in range(1):
    l = list(input().split(" "))
a = int(l[0])
b = int(l[1])
c = int(l[2])
d = int(l[3])
print(mini(a,b,c,d))
