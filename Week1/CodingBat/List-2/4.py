def sum13(nums):    
    sum = 0
    for x in range (len(nums)):
        if nums[x] != 13:
            sum = sum + nums[x]
        elif nums[x] == 13 and x < len(nums)-1:
            nums[x]= 0
            nums[x+1]= 0
    return sum 
