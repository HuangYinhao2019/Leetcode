##动态规划
def numberOfWays(num_people):
    dp_ary = {}
    dp_ary[0] = 1
    dp_ary[2] = 1
    dp_ary[4] = 2
    n = num_people

    for i in range(6, n + 1, 2):
        left = 0
        right = i - 2 - left
        dp_ary[i] = 0
        while left <= i - 2:
            dp_ary[i] = (dp_ary[i] + dp_ary[left] * dp_ary[right]) % 1000000007
            left += 2
            right -= 2
    return int(dp_ary[n] % 1000000007)

