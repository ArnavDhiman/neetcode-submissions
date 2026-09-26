class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, (rows*cols)-1
        
        while start <= end:
            mid = start + (end - start) // 2
            i, j = mid // cols, mid % cols
            # print(start, end, i, j, rows, cols)
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
