class Solution:
    def isValidSudoku(self, board):

        # Create a set for every row
        rows = [set() for _ in range(9)]

        # Create a set for every column
        cols = [set() for _ in range(9)]

        # Create a set for every 3 × 3 box
        boxes = [set() for _ in range(9)]

        # Visit every cell in the Sudoku board
        for r in range(9):
            for c in range(9):

                # Ignore empty cells
                if board[r][c] == ".":
                    continue

                # Current number
                num = board[r][c]

                # Find which 3 × 3 box this cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # If number already exists in the row,
                # the Sudoku is invalid
                if num in rows[r]:
                    return False

                # If number already exists in the column,
                # the Sudoku is invalid
                if num in cols[c]:
                    return False

                # If number already exists in the 3 × 3 box,
                # the Sudoku is invalid
                if num in boxes[box_index]:
                    return False

                # Store the number in its row
                rows[r].add(num)

                # Store the number in its column
                cols[c].add(num)

                # Store the number in its 3 × 3 box
                boxes[box_index].add(num)

        # No duplicates were found
        return True
        #leave 1