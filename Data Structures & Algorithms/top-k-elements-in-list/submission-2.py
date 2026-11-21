class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        see = defaultdict(int)
        lis = []
        for num in nums:
            see[num] += 1
        for num, cnt in see.items():
            lis.append([cnt, num])
        lis.sort()

        res = []
        while len(res) < k:
            res.append(lis.pop()[1])
        return res