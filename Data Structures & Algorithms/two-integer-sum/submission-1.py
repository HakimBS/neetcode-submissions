class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group = {}
        for i, num in enumerate(nums):
            diff= target-num
            if diff in group:
                return [group[diff],i]
            group[num] = i
        return []

        