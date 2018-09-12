def pos_neg(a, b, negative):
  if a*b<0 and negative is False:
    return True
  if a<0 and b<0 and negative is True:
    return True
  return False
