def oddCells(n, m, indices):
    """
    :type n: int
    :type m: int
    :type indices: List[List[int]]
    :rtype: int
    """
    arr = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(len(indices)):
        arr[indices[i][0]][indices[i][1]] += 1
    for i in range(n):
        for j in range(m):
            a = 0
            for q in range(n):
                a += arr[q][j]
            for p in range(m):
                a += arr[i][p]
            if a % 2 == 1:
                ans += 1
    return ans

indices = [[0,1],[1,1]]
n = 2
m = 3
print(oddCells(n,m,indices))