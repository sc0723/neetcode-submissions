class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for s in strs:
            key = ('').join(sorted(s))
            if key not in track:
                track[key] = [s]
            else:
                track[key].append(s)

        res = []
        for t in track.values():
            res.append(t)
        return res
