class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        if len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a
        res = ""
        c = False
        while i < len(a):
            if a[~i] == "1" and b[~i] == "1":
                if c:
                    res = "1" + res
                else:
                    c = True
                    res = "0" + res
            elif a[~i] == b[~i] == "0":
                if c:
                    res = "1" + res
                    c = False
                else:
                    res = "0" + res
            else:
                # 0 and 1
                if c:
                    res = "0" + res
                else:
                    res = "1" + res
            i += 1
        # Examine carrier bit and the first bit
        # print(res)
        if c:
            res = "1" + res
        return res
