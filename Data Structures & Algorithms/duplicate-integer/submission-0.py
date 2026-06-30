class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         ws = set(nums)
         return len(nums) > len(ws)