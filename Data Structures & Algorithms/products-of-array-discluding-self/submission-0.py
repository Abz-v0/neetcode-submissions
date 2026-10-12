class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        l_mul = 1
        for i in range(n):
            res[i] = l_mul
            l_mul *= nums[i]

        r_mul = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r_mul
            r_mul *= nums[i]
        
        return res