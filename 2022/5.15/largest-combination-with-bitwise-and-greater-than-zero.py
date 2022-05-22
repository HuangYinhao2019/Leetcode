class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        s = [0 for _ in range(100)]
        for i in range(len(candidates)):
            k = candidates[i]
            index = 0
            while k > 0:
                if k % 2 == 1:
                    s[index] += 1
                k = k >> 1
                index += 1
        res = 1
        for i in range(len(s)):
            res = max(res, s[i])
        return res

Solution.largestCombination(Solution, [16,17,71,62,12,24,14])