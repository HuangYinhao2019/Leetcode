def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    st = []
    p = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            st.append(s[i])
            p += 1
        elif s[i] == ')':
            if p != 0:
                p -= 1
            elif p == 0:
                s = s[:i] + s[i+1:]
                i -= 1
        i += 1
    st = []
    p = 0
    j = -1
    while j + len(s) >= 0:
        if s[j] == ')':
            st.append(s[j])
            p += 1
        elif s[j] == '(':
            if p != 0:
                p -= 1
            elif p == 0:
                s = s[:j+len(s)] + s[len(s) + j + 1:]
                j += 1
        j -= 1
    return s

s = "))(("
print(minRemoveToMakeValid(s))