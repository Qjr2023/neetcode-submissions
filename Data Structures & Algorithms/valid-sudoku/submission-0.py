class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            nums = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num not in nums and 0 < num < 10:
                        nums.add(num)
                    else:
                        return False
        
        for i in range(len(board[0])):
            nums = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    num = int(board[j][i])
                    if num not in nums and 0 < num < 10:
                        nums.add(num)
                    else:
                        return False
        
        for box_x in range(0, 9, 3):
            for box_y in range(0, 9, 3):
                nums = set()
                for i in range(box_x, box_x + 3): 
                    for j in range(box_y, box_y + 3):
                        if board[i][j] != ".":
                            num = int(board[i][j])
                            if num not in nums and 0 < num < 10:
                                nums.add(num)
                            else:
                                return False
        return True


        
        