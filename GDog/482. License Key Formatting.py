class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = "".join(S.split("-")).upper()[::-1]
        res = ""
        for i in range(len(S)):
            res += S[i]
            if (i + 1) % K == 0 and i < len(S) - 1:
                res += "-"
        return res[::-1]
