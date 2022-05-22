class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        res = 0
        for i in range(len(number)):
            if number[i] == digit:
                res = max(res, int(number[:i] + number[i + 1:]))
        return str(res)

print(Solution.removeDigit(Solution, "1231", "1"))