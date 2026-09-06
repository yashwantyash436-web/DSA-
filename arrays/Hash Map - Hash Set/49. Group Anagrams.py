class Solution(object):
    def groupAnagrams(self, strs):
        # Type hints and defaultdict imports are removed for Python 2 compatibility
        sMap = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in sMap:
                sMap[sorted_s] = []
            sMap[sorted_s].append(s)
        
        return sMap.values()
        