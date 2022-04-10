def numRollsToTarget(d, f, target):
    """
    :type d: int
    :type f: int
    :type target: int
    :rtype: int
    """
    arr = [0] * d
    for i in range(d):
        arr[i] = [0] * 1000
    for j in range(f):
        arr[0][j] = 1
    for i in range(1, d):
        arr[i][0] = 0
        S = 0
        for j in range(1, f + 1):
            S += arr[i - 1][j - 1]
            S = S % (1000000007)
            arr[i][j] = S
        for j in range(f + 1, 1000):
            S -= arr[i - 1][j - f - 1]
            S += arr[i - 1][j - 1]
            S = S % (1000000007)
            arr[i][j] = S
    res = arr[d - 1][target - 1] % (1000000007)
    return res

print(numRollsToTarget(30,30,500))