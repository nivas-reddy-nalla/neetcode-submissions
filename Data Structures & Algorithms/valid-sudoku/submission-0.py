class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i:set() for i in range(9)}
        column_map = {i:set() for i in range(9)}
        block_map = {i:set() for i in range(9)}

        for row in range(9):
            for col in range(9):
                cell_val = board[row][col]
                if cell_val == ".":
                    continue
                block = (row//3)*3 + (col//3)
                if (cell_val in row_map[row]) or (cell_val in column_map[col]) or (cell_val in block_map[block]):
                    return False
                row_map[row].add(cell_val)
                column_map[col].add(cell_val)
                block_map[block].add(cell_val)
        return True