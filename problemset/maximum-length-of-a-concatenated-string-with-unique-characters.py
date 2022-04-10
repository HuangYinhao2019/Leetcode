def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    Max = -1
    s = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        s[i] = set(arr[i])
        if len(s[i]) != len(arr[i]):
            s[i] = set()
        if len(s[i]) > Max:
            Max = len(s[i])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if len(s[i] & s[j]) == 0:
                if len(s[i]) + len(s[j]) > Max:
                    Max = len(s[i]) + len(s[j])
    return Max

arr = ["un","iq","ue"]
print(maxLength(arr))