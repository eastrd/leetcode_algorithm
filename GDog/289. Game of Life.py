class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid_cell(board, x, y):
            if board[x][y] in [1,2,3,4,5,6,7,8]:
                return 1
            else:
                return 0
        
        def search(board, x, y):
            count = 0
            if x > 0:
                count += is_valid_cell(board, x-1, y)
            if x < len(board) - 1:
                count += is_valid_cell(board, x+1, y)
            if y > 0:
                count += is_valid_cell(board, x, y-1)
            if y < len(board[0]) - 1:
                count += is_valid_cell(board, x, y+1)
            if x > 0 and y > 0:
                count += is_valid_cell(board, x-1, y-1)
            if x < len(board) - 1 and y < len(board[0]) - 1:
                count += is_valid_cell(board, x+1, y+1)
            if x > 0 and y < len(board[0]) - 1:
                count += is_valid_cell(board, x-1, y+1)
            if x < len(board) - 1 and y > 0:
                count += is_valid_cell(board, x+1, y-1)
            return count
        if not board:
            return
        height = len(board)
        width = len(board[0])
        for x in range(height):
            for y in range(width):
                count = search(board, x, y)
                if count == 3 and board[x][y] == 0:
                    board[x][y] = "x"
                elif board[x][y] == 1:
                    board[x][y] = count if count > 0 else 1
        
        for x in range(height):
            for y in range(width):
                if board[x][y] in ["x", 2, 3]:
                    board[x][y] = 1
                else:
                    board[x][y] = 0
