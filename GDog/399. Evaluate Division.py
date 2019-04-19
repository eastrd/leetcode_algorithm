class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find_path(s, e, graph):
            visited = {}
            traverse = []
            # print(s, e)
            # Check if exists
            if s not in graph or e not in graph:
                return -1.0
            # BFS search
            traverse.append((s, 1.0))
            while traverse:
                node, product = traverse.pop()
                visited[node] = True
                if node == e:
                    return product
                for i, weight in graph[node]:
                    if i not in visited:
                        traverse.append((i, weight * product))
            # Nodes can exist but might not be connected to each other
            return -1.0
        
        # Build the graph
        graph = {}
        for i in range(len(equations)):
            s, e = equations[i]
            if s not in graph:
                graph[s] = [(e, values[i])]
            else:
                graph[s].append((e, values[i]))
            if e not in graph:
                graph[e] = [(s, 1/values[i])]
            else:
                graph[e].append((s, 1/values[i]))
        
        res = []
        
        for s, e in queries:
            res.append(find_path(s, e, graph))
            
        return res
                    
