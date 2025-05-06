from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: 
            return
        rows = len(board)
        cols = len(board[0])
        surrounded = []
        def dfs(r, c):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for (dr, dc) in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc)
                


        