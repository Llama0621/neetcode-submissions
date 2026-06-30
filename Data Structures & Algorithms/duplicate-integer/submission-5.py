class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        comp = set(nums)
        if len(nums) > len(comp):
            return True
        return False