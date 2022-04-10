def xorQueries(arr, queries):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    xo = [0] * (len(arr) + 1)
    xo[0] = 0
    xo[1] = arr[0]
    for i in range(1,len(arr)):
        xo[i+1] = xo[i] ^ arr[i]
    ans = [0] * len(queries)
    for i,q in enumerate(queries):
        ans[i] = xo[q[1]+1] ^ xo[q[0]]
    return ans

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]

print(xorQueries(arr,queries))