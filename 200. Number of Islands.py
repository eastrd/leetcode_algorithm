class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            # Remove all of the adjacent grid to 0
            if -1 < x < len(grid) and -1 < y < len(grid[x]) and grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x+1, y)
                dfs(x, y+1)
                dfs(x-1, y)
                dfs(x, y-1)
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i, j)
        return counter
