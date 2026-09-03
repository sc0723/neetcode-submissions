class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key will be the sorted string, value will be an array of all strings with that sorted value
        track = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in track:
                track[key].append(s)
            else:
                track[key] = [s]
        
        res = []
        for i in track.values():
            res.append(i)
        
        return res
