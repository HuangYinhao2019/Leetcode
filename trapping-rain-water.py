def trap(height):
    stack = []
    stack_index = []
    v = 0
    for i in range(len(height)):
        if len(stack) == 0 or height[i] < stack[-1]:
            stack.append(height[i])
            stack_index.append(i)
        else:
            while height[i] >= stack[-1]:
                bottom = stack.pop()
                stack_index.pop()
                if len(stack) == 0:
                    break
                if height[i] > stack[-1]:
                    high = stack[-1]
                else:
                    high = height[i]
                v += (high - bottom) * (i - stack_index[-1] - 1)
            stack.append(height[i])
            stack_index.append(i)
    return v

height = [3,1,1,0,0,1,4,5,1,1,3]
print(trap(height))