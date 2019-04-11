class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.score = 0
        def dfs(elem, layer):
            for e in elem:
                if e.isInteger():
                    self.score += e.getInteger() * layer
                else:
                    dfs(e.getList(), layer+1)
        dfs(nestedList, 1)
        return self.score
