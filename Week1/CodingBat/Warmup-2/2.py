def front_times(str, n):
  l = 3
  if l>len(str):
    l = len(str)
  front = str[:l]
  result=""
  for x in range (n):
    result = result+result
  return result
  
  
