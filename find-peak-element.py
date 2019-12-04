def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = len(nums)-1
    mid = (int)((l+r)/2)
    while mid > 0 and mid < len(nums) - 1:
        mid = (int)((l + r) / 2)
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        else:
            if nums[mid] < nums[mid-1]:
                r = mid
            else:
                l = mid
    return mid

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))