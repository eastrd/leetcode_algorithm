class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        
        # s >= len(2)
        st = [s[0]]
        for i in range(1, len(s)):
            if s[i] in [")", "]", "}"]:
                left = st.pop()
                if left + s[i] not in ["()", "[]", "{}"]:
                    return False
            else:
                st.append(s[i])
        return not st
