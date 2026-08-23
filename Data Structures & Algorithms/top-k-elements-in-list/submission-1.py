class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ronaldo = {}
        for num in nums:
            if num in ronaldo:
                ronaldo[num] += 1
            else:
                ronaldo[num]=1
        messi = sorted(ronaldo,key = lambda x : ronaldo[x] ,reverse=True)
        return messi[:k]
            
            
        