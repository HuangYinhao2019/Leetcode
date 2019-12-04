def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = [[1]]
    n = 0
    ans = nums[0]
    for i in range(len(nums)):
        if nums[i] != 0:
            arr[n].append(nums[i]*arr[n][-1])
        else:
            if ans < 0:
                ans = 0
            arr.append([1])
            n += 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < 0:
                p = arr[i][j]
                break
            p = 1
        p2 = 0
        for k in range(len(arr[i])-1,j,-1):
            if arr[i][k] < 0:
                p2 = arr[i][k]
                break
        for j in range(len(arr[i])-1,0,-1):
            if arr[i][j] > 0:
                if arr[i][j] > ans:
                    ans = arr[i][j]
                break
        if p2/p > ans and p2 != 0:
            ans = (int)(p2/p)
    return ans
nums = [-2]
print(maxProduct(nums))