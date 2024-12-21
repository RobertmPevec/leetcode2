# o(n^2) solution:
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        isvalid = True
        for row in board:
            temp_list = []
            for numb in row:
                if numb != '.':
                    temp_list.append(numb)
            if len(set(temp_list)) != len(temp_list):
                isvalid = False
        if isvalid:
            for i in range(9):
                temp_list = []
                for j in range(9):
                    if board[j][i] != '.':
                        temp_list.append(board[j][i])
                if len(set(temp_list)) != len(temp_list):
                    isvalid = False
        if isvalid:
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    temp_list = []
                    for i in range(box_row, box_row + 3):
                        for j in range(box_col, box_col + 3):
                            if board[i][j] != '.':
                                temp_list.append(board[i][j])
                    if len(set(temp_list)) != len(temp_list):
                        isvalid = False
        return isvalid

# optimal O(1) solution
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True