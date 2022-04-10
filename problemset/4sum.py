def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    AB = {}
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] not in AB:
                AB[A[i] + B[j]] = 1
            else:
                AB[A[i] + B[j]] += 1
    ans = 0

    for i in range(len(C)):
        for j in range(len(D)):
            if 0 - C[i] - D[j] in AB:
                ans += AB[0 - C[i] - D[j]]
    return ans

def fourSum(nums, target):
    nums.sort()
    result = list()
    nums_len = len(nums)
    if nums_len < 4:
        return result
    if nums[0] * 4 > target or nums[nums_len - 1] * 4 < target:
        return result

    nums_map = {}
    for i in range(nums_len - 1, 0, -1):
        if i < nums_len - 1 and nums[i] == nums[i + 1]:
            continue
        for j in range(i - 1, -1, -1):
            if j < i - 1 and nums[j] == nums[j + 1]:
                continue
            if nums[i] + nums[j] not in nums_map:
                nums_map[nums[i] + nums[j]] = [[j, i]]
            else:
                nums_map[nums[i] + nums[j]].append([j, i])

    for i in range(nums_len - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, nums_len - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            dif = target - nums[i] - nums[j]
            if dif not in nums_map:
                continue
            else:
                for num in nums_map[dif]:
                    if num[0] > j:
                        result.append([nums[i], nums[j], nums[num[0]], nums[num[1]]])
    return result

def findNsum(nums, l, r, target, N, result, results):  #多数求和
    if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:
        return
    # two pointers solve sorted 2-sum problem
    if N == 2:
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(l, r + 1):
            if i == l or (i > l and nums[i - 1] != nums[i]):
                findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

