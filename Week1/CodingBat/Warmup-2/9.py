def string_match(a, b):
  x = min(len(a), len(b))
  cnt = 0
  for i in range(x-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      cnt = cnt + 1
  return cnt
