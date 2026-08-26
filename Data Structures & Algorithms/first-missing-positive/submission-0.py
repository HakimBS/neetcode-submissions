class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        yasmine = 1
        for num in nums:
            if num > 0 and yasmine == num:
                yasmine += 1
        return yasmine
        