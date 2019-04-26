class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],            
        }
        
        res = []
        # For each new set of chars, add them into a new copy into the existing ones
        for d in digits:
            temp = []
            if res:
                temp.extend(res)
                res = []
                for c in table[d]:
                    for word in temp:
                        res.append(word + c)
            else:
                res.extend([c for c in table[d]])
        
        return res
