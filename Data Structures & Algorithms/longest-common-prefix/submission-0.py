class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, char in enumerate(strs[0]):
            for other_str in strs[1:]:
                if i == len(other_str) or other_str[i] != char:
                    return res
            res += strs[0][i]
        return res


        