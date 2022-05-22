class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [words[0]]
        for i in range(1, len(words)):
            s0 = [0 for _ in range(26)]
            s1 = [0 for _ in range(26)]
            for j in range(len(words[i - 1])):
                s0[ord(words[i-1][j]) - ord('a')] += 1
            for j in range(len(words[i])):
                s1[ord(words[i][j]) - ord('a')] += 1
            fl = True
            for k in range(26):
                if s0[k] != s1[k]:
                    fl = False
            if fl == False:
                res.append(words[i])
        return res

Solution.removeAnagrams(Solution, ["abba","baba","bbaa","cd","cd"])
