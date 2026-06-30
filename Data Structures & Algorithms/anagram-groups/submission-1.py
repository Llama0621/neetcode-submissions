class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis1 = []
        used = set()
        for i, word1 in enumerate(strs):
            if i in used:
                continue
            lis2 = [word1]
            used.add(i)
            for j, word2 in enumerate(strs[i+1:], start=i+1):
                if len(word1) != len(word2) or j in used:
                    continue
                else:
                    dic_1, dic_2 = {}, {}
                    for char in word1:
                        dic_1[char] = dic_1.get(char, 0) + 1
                    for char in word2:
                        dic_2[char] = dic_2.get(char, 0) + 1 
                    if dic_1 == dic_2:
                        lis2.append(word2)
                        used.add(j)
            lis1.append(lis2)
        return lis1     