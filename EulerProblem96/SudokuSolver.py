import re
import sys
class SudokuSolver:

    def __init__(self):
        self.board = [['0' for i in range(9)] for j in range(9)]
        self.ReadFile()
        self.solved = False

    def ReadFile(self):
        try:
           b  = open(sys.argv[1]).read()
           self.ReadBoard(b)
        except IOError:
            print("Could not open file")
            sys.exit(1)
        except IndexError:
            print("Invalid file")
            sys.exit(1)

    def ReadBoard(self, board):
        for i in range(0,9):
            l = board.splitlines()[i]
            l = re.sub('[^0-9]', '',l)
            for j in range(0,9):
                self.board[i][j] = l[j]

    def Solve(self, x, y):
        if self.board[x][y] != '0':
            self.GoToNext(x,y)
            return
        for k in range(1,10):
            if self.solved:
                return
            self.board[x][y] = str(k)
            if self.Check(x,y,str(k)):
                self.GoToNext(x,y)
            if k == 9 and not self.solved: 
                self.board[x][y] = '0'
                return
                    



    def Check(self, x, y, val):
        ## check row
        if self.board[x].count(val) > 1:
            return False
        ## check column
        for i in range(0,9):
            if self.board[i][y] == val and i != x:
                return False
        ## check 3x3 grid
        for i in range(0,3):
            for j in range(0,3):
                xTemp = (((x) // 3) * 3) + i
                yTemp = (((y) // 3) * 3) + j
                currVal = self.board[xTemp][yTemp]
                if currVal == val and xTemp != x and yTemp != y:
                    return False
        return True

            

    def GoToNext(self, x, y):
        if self.solved:
            return
        if x <= 8 and y < 8:
            self.Solve(x , y + 1)
        elif x < 8 and y == 8:
            self.Solve(x + 1, 0)
        elif x == 8 and y == 8:
            self.Finalize()

    def printBoard(self):
        result = ''
        for i in range(9):
            if (i) % 3 == 0 and i > 0:
                result += '\n\n'
            elif i > 0:
                result += '\n'
            for j in range(9):
                if (j + 1) % 3 == 0:
                   result += self.board[i][j] + '   '
                else:
                   result += self.board[i][j] + ' '
        print(result)




    def Finalize(self):
       self.printBoard()
       self.solved = True






