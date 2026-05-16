class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        out = []
        for i in strs:
            sor = "".join(sorted(i))
            if sor in hm:
                hm[sor].append(i)
            else:
                hm[sor] = [i]
        for i in hm.values():
            out.append(i)
        return out