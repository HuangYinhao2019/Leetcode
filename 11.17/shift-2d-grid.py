def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    arr = []
    for i in range(len(grid)):
        arr = arr + grid[i]
    l = len(grid) * len(grid[0])
    k %= l
    p = arr[len(arr)-k:] + arr[:len(arr)-k]
    i = 0
    for r in range(len(grid)):
        for l in range(len(grid[0])):
            grid[r][l] = p[i]
            i += 1
    return grid

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(shiftGrid(grid,k))