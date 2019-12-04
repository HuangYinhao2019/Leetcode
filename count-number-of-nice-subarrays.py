def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l, r = 0, 0
    o = 0
    i, j = 0, 0
    ans = 0
    while i < len(nums) and j < len(nums):
        if nums[j] % 2 == 0 and i == j:
            l += 1
            i += 1
            j += 1
        elif nums[j] % 2 == 0:
            j += 1
        elif nums[j] % 2 == 1:
            o += 1
            if o < k:
                j += 1
            else:
                ri = j + 1
                while ri < len(nums) and nums[ri] % 2 == 0:
                    ri += 1
                    r += 1
                ans += (l+1) * (r+1)
                l = 0
                r = 0
                i += 1
                o -= 1
                j += 1
                while i < len(nums):
                    if nums[i] % 2 == 0:
                        i += 1
                        l += 1
                    else:
                        break
    return ans

a = [2,2,2,1,2,2,1,2,2,2]
print(numberOfSubarrays(a,1))