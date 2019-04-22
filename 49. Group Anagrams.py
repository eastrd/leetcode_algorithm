class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return strs
        ana_dict = {}
        for w in strs:
            key = "".join(sorted(w))
            if key in ana_dict:
                ana_dict[key].append(w)
            else:
                ana_dict[key] = [w]
        
        res = []
        for k in ana_dict:
            res.append(ana_dict[k])
        
        return res
