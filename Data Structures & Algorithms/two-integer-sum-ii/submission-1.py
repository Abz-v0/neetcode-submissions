class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)

        while l < r:
            cur_sum = numbers[l - 1] + numbers[r - 1]
            if cur_sum == target:
                return [l, r]
            elif cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1

        return [l, r]


                    