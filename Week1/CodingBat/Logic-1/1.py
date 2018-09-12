def cigar_party(cigars, is_weekend):
  if is_weekend is False:
    if cigars>=40 and cigars<=60:
      return True
  
  else:
    if cigars>=40:
      return True
  return False
