class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        return self.dfs(grid, 0, 0, 0, 0)
    def dfs(self, grid, i, j, ls, rs):
        if i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == '(':
            ls += 1
        else:
            rs += 1
        if ls > (len(grid) + len(grid[0]) - 1) / 2 or rs > (len(grid) + len(grid[0]) - 1) / 2 or rs > ls:
            return False
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        else:
            return self.dfs(grid, i + 1, j, ls, rs) or self.dfs(grid, i, j + 1, ls, rs)

s = Solution()
s.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]])