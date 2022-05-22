class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        res = {}
        for i in range(len(nums)):
            now = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                   now = now + 1
                if now > k:
                    break
                flag = True
                if j+1-i not in res:
                    res[j+1-i] = [nums[i:j+1]]
                    continue
                for q in range(len(res[j+1-i])):
                    if res[j+1-i][q] == nums[i:j+1]:
                        flag = False
                        break
                if flag:
                    res[j+1-i].append(nums[i:j+1])
        sum = 0
        for i in res:
            sum += len(res[i])
        return sum

print(Solution.countDistinct(Solution, [2,3,3,2,2], 2, 2))
print(Solution.countDistinct(Solution, [1,2,3,4], 4, 1))