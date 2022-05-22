class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        res = 10000000
        last = {}
        for i in range(len(cards)):
            if cards[i] not in last:
                last[cards[i]] = i
            else:
                res = min(i - last[cards[i]] + 1, res)
            last[cards[i]] = i
        if res == 10000000:
            res = -1
        return res

print(Solution.minimumCardPickup(Solution, [3,4,2,3,4,7]))
print(Solution.minimumCardPickup(Solution, [1,0,5,3]))