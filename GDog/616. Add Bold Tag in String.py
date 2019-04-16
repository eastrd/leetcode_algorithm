class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        dict = sorted(dict, key = lambda x: -len(x))
        bold_list = [False] * len(s)
        res = ""
        for i in range(len(s)):
            for w in dict:
                if w == s[i:i + len(w)]:
                    for j in range(i, i + len(w)):
                        bold_list[j] = True
                    break
        # print(bold_list)
        for i in range(len(bold_list)):
            if bold_list[i]:
                if i == 0 or not bold_list[i-1]:
                    res += "<b>"
                res += s[i]
                if i == len(bold_list) - 1 or not bold_list[i+1]:
                    res += "</b>"

            else:
                res += s[i]
        return res
                    
        
