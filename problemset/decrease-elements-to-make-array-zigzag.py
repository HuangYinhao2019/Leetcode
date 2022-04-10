def movesToMakeZigzag(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans1 = 0
    ans2 = 0
    for i in range(0,len(nums),2):
        if i == 0:
            d = max(-1,nums[i]-nums[i+1])
        else:
            if i == len(nums)-1:
                d = max(-1,nums[i]-nums[i-1])
            else:
                d = max(-1,nums[i]-nums[i-1],-1,nums[i]-nums[i+1])
        ans1 += d+1
    for i in range(1,len(nums),2):
        if i == 0:
            d = max(-1,nums[i]-nums[i+1])
        else:
            if i == len(nums)-1:
                d = max(-1,nums[i]-nums[i-1])
            else:
                d = max(-1,nums[i]-nums[i-1],-1,nums[i]-nums[i+1])
        ans2 += d+1
    return min(ans1,ans2)

g = [3,10,7,9,9,3,6,9,4]
print(movesToMakeZigzag(g))