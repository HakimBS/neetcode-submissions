class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefixe =[1] * n
        suffixe = [1] * n
        for i in range (1,n):
            prefixe[i] = prefixe[i-1] * nums[i-1]
        for i in range (n-2,-1,-1):
            suffixe[i] = suffixe[i+1] * nums[i+1]
        ronaldo = []
        for i in range (n):
            ronaldo.append(suffixe[i]*prefixe[i])
        return ronaldo