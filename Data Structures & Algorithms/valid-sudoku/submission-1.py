class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for n in row:
                if n == ".":
                    continue
                if n in seen:
                    return False
                seen.add(n)

        cols = range(len(board[0]))
        for i in cols:
            seen = set()
            for n in range(len(board)):
                if board[n][i] == ".":
                    continue
                if board[n][i] in seen:
                    return False
                seen.add(board[n][i])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])

        return True
