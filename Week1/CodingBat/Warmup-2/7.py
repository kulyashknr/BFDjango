def array_front9(nums):
  a = len(nums)
  if a>4:
    a=4
  for x in range(a):
    if nums[x] == 9:
      return True
  return False
