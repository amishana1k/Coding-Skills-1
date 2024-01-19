class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        t = 0
        r = []
        for i in range(len(nums[t])):
            if t == 0 or t == 3:
                r.append(nums[t][i])
                t += 1
            else:
                r.append(nums[t][i])
                t += 1
        r = sorted(r)
        return r[-1]
