def minInsertions(s):
    """
    :type s: str
    :rtype: int
    """
    dp = [[0] * 501 for _ in range(501)]
    y = s[::-1]
    for i in range(len(s)):
        for j in range(len(y)):
            p = 0
            if s[i] == y[j]:
                p = 1
            dp[i + 1][j + 1] = max(dp[i][j] + p, max(dp[i + 1][j], dp[i][j + 1]))
    return len(s) - dp[len(s)][len(y)]

print(minInsertions("leetcode"))