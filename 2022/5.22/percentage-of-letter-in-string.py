class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            if s[i] == letter:
                sum += 1
        res = int(sum * 100 / len(s))
        return res