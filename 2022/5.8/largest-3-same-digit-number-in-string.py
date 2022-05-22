class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        mmax = -1
        for i in range(2, len(num)):
            if num[i] == num[i - 1] and num[i - 1] == num[i - 2]:
                mmax = max(mmax, int(num[i-2:i+1]))
        if mmax == -1:
            return ""
        elif mmax == 0:
            return "000"
        else:
            return str(mmax)

print(Solution.largestGoodInteger(Solution, "6777133339"))