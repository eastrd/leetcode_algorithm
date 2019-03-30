class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = {}
        for i in range(n):
            if not res:
                res["()"] = 0
            else:
                temp = {}
                for p in res:
                    for i in range(len(p)):
                        copy = p
                        copy = copy[:i] + "()" + copy[i:]
                        if copy not in temp:
                            temp[copy] = 0
                res = temp
        return list(res.keys())
