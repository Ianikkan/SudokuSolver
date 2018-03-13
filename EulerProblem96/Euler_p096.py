from SudokuSolver import SudokuSolver
import re
import sys
class Sudoku(SudokuSolver):
    def __init__(self):
        self.sum = 0
        super().__init__()


    def ReadFile(self):
      boardsFile = open(r'./files/p096_sudoku.txt')
      boards = boardsFile.read();
      boardsArr = [x for x in re.compile('Grid\s\d\d').split(boards) if x]
      for b in boardsArr:
          b = b.strip("\n")
          self.ReadBoard(b)
          self.solved = False
          self.Solve(0,0)
          self.addToSum()
      self.FinalizeAll()
       
          

      
    def MakeIndividual(self, b):
        self.board = [x for x in b.split('\n') if x]
    
           

    def addToSum(self):
         self.sum +=  int(''.join(self.board[0][:3]))




    def Finalize(self):
        self.solved = True

    def FinalizeAll(self):
        print(self.sum)

    def solveAll(self):
      for b in self.boardsArr:
          self.MakeIndividual(b)
          self.Solve(0,0)
        

su = Sudoku()