def numWays(steps, arrLen):
    """
    :type steps: int
    :type arrLen: int
    :rtype: int
    """
    if arrLen == 1:
        return 1
    if arrLen > steps:
        arrLen = steps + 1
    arr = [[0] * arrLen for _ in range(steps)]
    arr[0][0], arr[0][1] = 1, 1
    for i in range(1, steps):
        arr[i][0] = (arr[i - 1][0] + arr[i - 1][1]) % 1000000007
        arr[i][-1] = (arr[i - 1][-1] + arr[i - 1][-2]) % 1000000007
        for j in range(1, arrLen - 1):
            arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1]) % 1000000007

    return arr[-1][0] % 1000000007

print(numWays(27,7))