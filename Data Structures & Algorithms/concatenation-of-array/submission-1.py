class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sum_list = []
        for i in range(2):
            for num in nums:
                sum_list.append(num)
        return sum_list
        