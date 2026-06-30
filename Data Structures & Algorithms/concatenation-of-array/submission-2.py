class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lis = []
        for i in range(2):
            for num in nums:
                lis.append(num)
        return lis
        