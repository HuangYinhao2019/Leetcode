def maxSumDivThree(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = sum(nums)
    d1, d2 = [], []
    for i in range(len(nums)):
        if nums[i] % 3 == 1:
            d1.append(nums[i])
        elif nums[i] % 3 == 2:
            d2.append(nums[i])
    d1.sort()
    d2.sort()
    if len(d1) % 3 == len(d2) % 3:
        return ans
    elif (len(d1) - len(d2)) % 3 == 1:
        if len(d1) == 0:
            return ans - d2[0] - d2[1]
        elif len(d2) == 0 or len(d2) == 1:
            return ans - d1[0]
        else:
            return max(ans - d2[0] - d2[1], ans - d1[0])
    else:
        if len(d2) == 0:
            return ans - d1[0] - d1[1]
        elif len(d1) == 0 or len(d1) == 1:
            return ans - d2[0]
        else:
            return max(ans - d1[0] - d1[1], ans - d2[0])

nums = [3,5,6,1,8]
print(maxSumDivThree(nums))