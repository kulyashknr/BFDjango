def max_end3(nums):
  if nums[0]>nums[2]:
    nums[1]=nums[0]
    nums[2]=nums[0]

  if nums[2]>=nums[0] :
    nums[0]=nums[2]
    nums[1]=nums[2]
  return nums