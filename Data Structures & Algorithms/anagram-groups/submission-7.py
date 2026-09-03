from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[''.join(sorted(s))].append(s)
        res = []
        for val in groups.values():
            res.append(val)
        
        return res
