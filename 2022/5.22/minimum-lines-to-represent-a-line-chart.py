class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        if len(stockPrices) == 1:
            return 0
        stockPrices = sorted(stockPrices, key=lambda l:l[0])
        res = 1
        x, y = stockPrices[1][0] - stockPrices[0][0], stockPrices[1][1] - stockPrices[0][1]
        for i in range(1, len(stockPrices)):
            x0, y0 = stockPrices[i][0] - stockPrices[i - 1][0], stockPrices[i][1] - stockPrices[i - 1][1]
            if x0 * y != y0 * x:
                res += 1
            x, y = x0, y0
        return res

print(Solution.minimumLines(Solution, [[3,6],[4,6],[7,6]]))