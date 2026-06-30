class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, char in enumerate(strs[0]):
            for other_strs in strs[1:]:
                if len(other_strs) == i or char != other_strs[i]:
                    return res
            res += strs[0][i]
        return res

        