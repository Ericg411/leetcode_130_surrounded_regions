from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: 
            return
        rows = len(board)
        cols = len(board[0])
        surrounded = []
        history = set()
        def dfs(r, c):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            sides = 0
            for (dr, dc) in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr,nc) not in history:
                    if nr == 0 or nr == rows or nc == 0 or nc == cols:
                        history.clear()
                        break 
                    history.add((nr, nc))
                    dfs(nr, nc)
                    sides += 1
            if sides == 0:
                for (hr, hc) in history:
                    board[hr][hc] = "X"


        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if board[r][c] == "O":
                    dfs(r, c)


        
        