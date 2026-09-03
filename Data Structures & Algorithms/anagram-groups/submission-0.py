class Solution:
    def checkAnagrams(self, str1, str2):
        s1 = {}
        for s in str1:
            if s not in s1:
                s1[s] = 1
            else:
                s1[s] += 1
        for c in str2:
            if c not in s1:
                return False
            s1[c] -= 1
            if s1[c] < 0:
                return False
        for i in s1:
            if s1[i] != 0:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dup = [False] * len(strs)
        if len(strs) == 1:
            t2 = []
            t2.append(strs[0])
            res.append(t2)
            return res
        else:
            for i in range(len(strs)):
                if not dup[i]:
                    t2 = []
                    t2.append(strs[i])
                    dup[i] = True
                    for j in range(i+1, len(strs)):
                        if not dup[j] and self.checkAnagrams(strs[i], strs[j]):
                            t2.append(strs[j])
                            dup[j] = True
                    res.append(t2)
            return res
