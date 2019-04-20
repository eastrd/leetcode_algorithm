class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        
        # Board is at least length 1
        width = len(board[0])
        height = len(board)
        
        if width * height < len(word):
            return False
        
        def dfs(x, y, path, letters):
            '''
            Base case:  No letters left
            Steps:      
                1. If x and y not specified, then search the grid and apply dfs on all occurrances
                2. If x and y specified, then check current coord and see if it's within boundary and if so
                    check if it's the letter
                3. Search surrounding blocks around given x & y and apply dfs on them
            '''
            if not letters:
                return True
            
            letter, letters = letters[0], letters[1:]
            
            # Check boundary
            if x < 0 or x >= height or y < 0 or y >= width or board[x][y] != letter or (x, y) in path:
                return False
            new_path = path + [(x, y)]
            return dfs(x+1, y, new_path, letters) or dfs(x-1, y, new_path, letters)\
                    or dfs(x, y-1, new_path, letters) or dfs(x, y+1, new_path, letters)
            
        
        for x in range(height):
            for y in range(width):
                if dfs(x, y, [], word):
                    return True
        return False
