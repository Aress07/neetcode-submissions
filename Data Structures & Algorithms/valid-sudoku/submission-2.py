class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] not in set1: 
                    set1.add(board[i][j])
                else:
                    return False
        
        for j in range(9):
            set2 = set()
            for i in range(9):
                if board[i][j] == ".": continue
                if board[i][j] not in set2:
                    set2.add(board[i][j])
                else:
                    return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                set3 = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == ".": continue
                        if board[i][j] not in set3: 
                            set3.add(board[i][j])
                        else: 
                            return False
        return True
            


