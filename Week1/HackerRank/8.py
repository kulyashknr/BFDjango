n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
while m in arr: arr.remove(m)
print(max(arr))
