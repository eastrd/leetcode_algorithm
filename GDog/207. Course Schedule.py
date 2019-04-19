class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # Construct Graph data structure
        checked = {}
        graph = {}
        for e, s in prerequisites:
            if s not in graph:
                graph[s] = [e]
            else:
                graph[s].append(e)
        
        def dfs(s):
            if s not in graph:
                return True
            if s in checked and checked[s] == 0:
                return False
            checked[s] = 0
            for n in graph[s]:
                if not dfs(n):
                    return False
            checked[s] = 1
            return True
        
        
        
        # Check cycles by BFS
        for n in graph:
            if not dfs(n):
                return False
        return True
