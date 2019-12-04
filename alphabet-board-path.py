def alphabetBoardPath(target):
    """
    :type target: str
    :rtype: str
    """
    al = [0] * 26
    c = 0
    for i in ("abcdefghijklmnopqrstuvwxyz"):
        al[ord(i) - 97] = c
        c += 1
    nowx = 0
    nowy = 0
    movex = 0
    movey = 0
    ans = ""
    for i in (target):
        tx = al[ord(i) - 97] % 5
        ty = (int)(al[ord(i) - 97] / 5)
        movex = tx - nowx
        movey = ty - nowy
        for j in range(-movex): #error1：先LU，再RD
            ans += "L"
        for j in range(-movey):
            ans += "U"
        for j in range(movex):
            ans += "R"
        for j in range(movey):
            ans += "D"
        ans += "!"
        nowx = tx
        nowy = ty
    return ans
print(alphabetBoardPath("codez"))