def count_evens(nums):
    cnt = 0
    for x in range (len(nums)):
        if nums[x]%2 == 0:
            cnt =  cnt+ 1
    return cnt
