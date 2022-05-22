class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        D = 1000000007
        dp = [1, 1]
        for i in range(1, len(pressedKeys)):
            dp.append(dp[-1])
            if pressedKeys[i] == pressedKeys[i - 1]:
                dp[-1] = (dp[-1] + dp[-3]) % D
                if i - 2 >= 0 and pressedKeys[i] == pressedKeys[i - 2]:
                    dp[-1] = (dp[-1] + dp[-4]) % D
                    if i - 3 >= 0 and (pressedKeys[i] == "7" or pressedKeys[i] == "9") and pressedKeys[i] == pressedKeys[i - 3]:
                        dp[-1] = (dp[-1] + dp[-5]) % D
        return dp[-1]