class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = "".join(S.split("-")).upper()[::-1]
        res = ""
        for i in range(len(S)):
            res += S[i]
            if (i + 1) % K == 0 and i < len(S) - 1:
                res += "-"
        return res[::-1]

    
    ###############################################
    # Optimized Version
    
    class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = "".join(S.split("-")).upper()
        res = ""
        first_len = len(S) % K
        
        for i in range(len(S)):
            res += S[i]
            if i < len(S) - 1 and (i + 1 == first_len or (i + 1 - first_len) % K == 0):
                res += "-"
        return res
