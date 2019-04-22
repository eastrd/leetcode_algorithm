class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        if not str:
            return
        s = e = 0
        for i in range(len(str) // 2):
            str[i], str[~i] = str[~i], str[i]
        if str[-1] != " ":
            str.append(" ")
        # Iterate through the list, when encounter a space, then record it as ending index, reverse s to e
        while True:
            if str[e] == " ":
                # Reverse s to e-1
                for i in range((e - s) // 2):
                    str[s + i], str[e-i-1] = str[e-i-1], str[s + i]
                s = e + 1
            e += 1
            
            if e == len(str):
                del str[-1]
                return
