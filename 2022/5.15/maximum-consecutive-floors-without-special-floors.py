class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        mmax = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            mmax = max(mmax, special[i] - special[i - 1] - 1)
        return mmax