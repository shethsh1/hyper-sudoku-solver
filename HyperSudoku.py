#################################################################
#                                                               #
#    Define any helper functions you need in this file only.    #
#    You will be handing in HyperSudoku.py, nothing else.       #
#                                                               #
#    A few test cases are provided in Test.py. You can test     #
#    Your code by running: (See the file for more details)      #
#               python Test.py                                  #
#    in the directory where the files are located.              #
#                                                               #
#    We're using Python 3.X this time.                          #
#                                                               #
#################################################################


class HyperSudoku:

    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """
        # returns True if its been solved false otherwise
        output = HyperSudoku.solverIfPossible(grid)
        if(output is False):
            return None
        return grid

    @staticmethod
    def solverIfPossible(grid):
        '''
        returns true if solved false otherwise
        '''
        # backtracking dfs method using stack
        stack = []
        value = HyperSudoku.findNext(grid, 0, 0)
        if(value == None):
            return True
        stack.append(value)
        while stack != []:
            k = stack[-1][2]
            valOne = stack[-1][0]
            valTwo = stack[-1][1]
            while k <= 9:
                
                # check if row is compatible
                # check if col is compatible
                # check if box is compatible
                # check if hypersudoko box is compatible 
                if(HyperSudoku.checkRow(grid, valOne, valTwo,  k) and 
                   HyperSudoku.checkCol(grid, valOne, valTwo,  k) and 
                   HyperSudoku.checkBox(grid, 3*(valOne//3), 3*(valTwo//3), k)):
                    # hypersudoku box is only applicable in these select columns / rows
                    if (valOne in [1, 2, 3, 5, 6, 7] and valTwo in [1, 2, 3, 5, 6, 7]):
                        if not(HyperSudoku.checkBox(grid, 4*(valOne//4)+1, 4*(valTwo//4)+1, k)):
                            # simply goes on to the next number unless it's 9 then it backtracks
                            if(k== 9):
                                grid[valOne][valTwo] = 0
                                stack.pop()
                                break
                            else:
                                k+=1
                                continue
                            
                    grid[valOne][valTwo] = k
                    value = HyperSudoku.findNext(grid, valOne, valTwo)
                    if(value is None):
                        return True
                    stack[-1][2] = k
                    stack.append(value)
                    break
                else:
                    # simply goes on to the next number unless it's 9 then it back tracks
                    if(k== 9):

                        grid[valOne][valTwo] = 0
                        stack.pop()
                        break
                    else:
                        k+=1

        return False

    @staticmethod
    def findNext(grid, x, y):
        # to make it a bit quicker I let x and y be set
        for i in range(x, 9):
            for j in range(y, 9):
                if grid[i][j] == 0:
                    return [i, j, 1]
            y = 0

    @staticmethod
    def checkBox(grid, r, c, k):
        for i in range(3):
            for j in range(3):
                if(grid[i+r][j+c] == k):
                    return False
        return True

    @staticmethod
    def checkRow(grid, r, c, k):
        rowSafe = True
        for i in range(9):
            rowSafe = k != grid[r][i]
            if(rowSafe is False):
                return False
        return rowSafe

    @staticmethod
    def checkCol(grid, r, c, k):
        colSafe = True
        for i in range(9):
            colSafe = k != grid[i][c]
            if(colSafe is False):
                return False
        return True

    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be
        used in marking. It is just to help you debug.

        Use as:     HyperSudoku.printGrid(grid)
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)


