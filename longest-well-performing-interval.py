def longestWPI(hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    arr = [0] * (len(hours) + 1)
    for i in range(len(hours)):
        if hours[i] <= 8:
            arr[i+1] = arr[i] - 1
        else:
            arr[i+1] = arr[i] + 1
    stack = []
    si = []
    for i in range(len(arr)):
        if len(stack) == 0 or arr[i] < stack[len(stack)-1]:
            stack.append(arr[i])
            si.append(i)
    ans = 0
    i = len(arr) - 1
    while stack and i > ans:
        if arr[i] - stack[len(stack)-1] > 0:
            if i - si[len(stack)-1] > ans:
                ans = i - si[len(stack)-1]
            stack.pop()
        else:
            i -= 1
    return ans
def maxWidthRamp(A):
    """
    :type A: List[int]
    :rtype: int
    """
    stack = []
    si = []
    for i in range(len(A)):
        if len(stack) == 0 or A[i] <= stack[len(stack)-1]:
            stack.append(A[i])
            si.append(i)
    ans = 0
    i = len(A)-1
    while stack and i > ans:
        if A[i] - stack[len(stack)-1] >= 0:
            if i - si[len(stack)-1] > ans:
                ans = i - si[len(stack)-1]
            stack.pop()
        else:
            i-=1
    return ans

# hours = [9,9,6,0,6,6,9,4,3]
# print(longestWPI(hours))

A=[9,8,1,0,1,9,4,0,4,1]
print(maxWidthRamp(A))