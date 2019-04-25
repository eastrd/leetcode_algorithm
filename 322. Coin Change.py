class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        
        # Amount > 0 and more than 1 coin amount
        
        mem = [float("inf")] * (amount + 1)
        
        for i in range(1, len(mem)):
            for j in coins:
                if i - j > 0 and mem[i-j] + 1 < mem[i]:
                    mem[i] = mem[i - j] + 1
                if i % j == 0 and i // j < mem[i]:
                    mem[i] = i // j
        # print(mem)
        return mem[-1] if mem[-1] != float("inf") else -1
