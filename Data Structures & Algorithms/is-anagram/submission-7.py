class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        for ch1 in s:
            if ch1 in hash1:
                hash1[ch1] += 1
            else:
                hash1[ch1] = 1
        for ch2 in t:
            if not ch2 in hash1:
                return False
            hash1[ch2] -= 1
            if hash1[ch2] < 0:
                return False
        return True
