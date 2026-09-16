class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][-1]:
                l = mid + 1

            elif target < matrix[mid][0]:
                r = mid - 1

            else:
                l1, r1 = 0, len(matrix[mid]) - 1
                while l1 <= r1:
                    m = (l1 + r1) // 2
                    if target == matrix[mid][m]: return True
                    elif target > matrix[mid][m]: l1 = m + 1
                    else: r1 = m - 1
                return False
        return False
