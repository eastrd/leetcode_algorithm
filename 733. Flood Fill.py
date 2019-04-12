class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.visited = []
        
        def dfs(x, y, colour):
            if -1 < x < len(image) and -1 < y < len(image[0]) and (x, y) not in self.visited and image[x][y] == colour:
                # print(x, y)
                self.visited.append((x, y))
                image[x][y] = newColor
                dfs(x+1, y, colour)
                dfs(x, y+1, colour)
                dfs(x-1, y, colour)
                dfs(x, y-1, colour)
                
    
        dfs(sr, sc, image[sr][sc])
        
        return image
