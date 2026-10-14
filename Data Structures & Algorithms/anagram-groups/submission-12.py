from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        ans = []

        for key, value in groups.items():
            ans.append(value)
        
        return ans
