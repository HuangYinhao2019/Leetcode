class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        le = []
        for i in range(len(capacity)):
            le.append(capacity[i] - rocks[i])
        le.sort()
        res = 0
        for i in range(len(le)):
            if additionalRocks >= le[i]:
                res += 1
                additionalRocks -= le[i]
        return res