def last2(str):
  if len(str) < 2:
    return 0
  
  l = str[len(str)-2:]
  cnt = 0
  
  for i in range(len(str)-2):
    subs = str[i:i+2]
    if subs == l:
      cnt = cnt + 1

  return cnt
