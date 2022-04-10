def freqAlphabets(s):
    """
    :type s: str
    :rtype: str
    """
    i = len(s) - 1
    ans = ""
    while i >= 0:
        if s[i] == '#':
            ans = str(chr(int(s[i-2:i]) + 96)) + ans
            i -= 3
        else:
            ans = str(chr(int(s[i]) + 96)) + ans
            i -= 1
    return ans

print(freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))