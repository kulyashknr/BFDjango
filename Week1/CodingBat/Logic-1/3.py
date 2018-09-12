def squirrel_play(temp, is_summer):
  if is_summer is False:
    if temp>=60 and temp<=90:
      return True
  else:
    if temp>=60 and temp<=100:
      return True
  return False
