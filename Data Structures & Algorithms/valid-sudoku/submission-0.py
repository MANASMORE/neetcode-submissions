class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for y in range(9)]
        box = [set() for z in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                digit = board[i][j]

                box_index = (i // 3)*3 + (j // 3)
                
                if digit in rows[i] or digit in cols[j] or digit in box[box_index]:
                    return False
                else:
                    rows[i].add(digit)
                    cols[j].add(digit)
                    box[box_index].add(digit)
        return True