def encode(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return ""
    else:
        ans = ""
        num += 1
        while num != 0:
            ans = str(num % 2) + ans
            num = int(num / 2)
        return ans[1:]

print(encode(5))