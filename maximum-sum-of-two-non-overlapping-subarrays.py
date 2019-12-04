def maxSumTwoNoOverlap(A, L, M):
    """
    :type A: List[int]
    :type L: int
    :type M: int
    :rtype: int
    """
    dp = [0] * 4
    for i in range(4):
        dp[i] = [0] * len(A)
    Sum = 0
    for i in range(L):
        Sum += A[i]
    max = Sum
    dp[0][L-1] = max
    for i in range(L,len(A)):
        Sum += A[i]
        Sum -= A[i-L]
        if Sum > max:
            max = Sum
        dp[0][i] = max

    Sum = 0
    for i in range(M):
        Sum += A[i]
    max = Sum
    dp[1][M-1] = max
    for i in range(M, len(A)):
        Sum += A[i]
        Sum -= A[i - M]
        if Sum > max:
            max = Sum
        dp[1][i] = max

    Sum = 0
    for i in range(len(A)-1,len(A)-L-1,-1):
        Sum += A[i]
    max = Sum
    dp[2][len(A)-L] = max
    for i in range(len(A)-L-1,-1,-1):
        Sum -= A[i+L]
        Sum += A[i]
        if Sum > max:
            max = Sum
        dp[2][i] = max

    Sum = 0
    for i in range(len(A) - 1, len(A) - M - 1, -1):
        Sum += A[i]
    max = Sum
    dp[3][len(A) - M] = max
    for i in range(len(A) - M - 1, -1, -1):
        Sum -= A[i + M]
        Sum += A[i]
        if Sum > max:
            max = Sum
        dp[3][i] = max

    res = 0
    for i in range(L,len(A)-M+1):
        if dp[0][i-1] + dp[3][i] > res:
            res = dp[0][i-1] + dp[3][i]
    for i in range(M,len(A)-L+1):
        if dp[1][i-1] + dp[2][i] > res:
            res = dp[1][i-1] + dp[2][i]
    return res

A = [8,20,6,2,20,17,6,3,20,8,12]
L = 5
M = 4
print(maxSumTwoNoOverlap(A,L,M))
