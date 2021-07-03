import copy
import random

class SudokuBoard:
    def __init__(self, board=None):
        """
            This class represents a Sudoku Board and its methods.
            
            Params
            ------
            board: It expects a 81 characters <string> object containing the numbers distribution 
                   in the board. Empty cells are represented with 0. If <None> is given, then an 
                   empty board will be created (9x9 board filled with 0's).
        """

        # Populate the board with 0's
        self.__resetBoard()

        # If board was given, copy it to the self.board attribute
        if board:
            for i in range(0,9):
                for j in range(0,9):
                    self.board[i][j] = int(board[(i*9) + j])
    

    def __resetBoard(self):
        """
            This private functions resets the board state. This is, fill it with 0's
            (empty spaces).
        """
        self.board = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]          
    

    def printBoard(self):
        """
            This method prints the board with the standard Sudoku format.
        """
        for i in range(9):
            if i%3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(9):
                if j%3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
    

    def boardAsString(self):
        """
            This method converts the board in a string.

            Returns
            -------
            - A <str> object which stores the board.
        """
        string = "".join([str(col) for row in self.board for col in row])
        return string


    def __findEmptySpace(self, board=None, emptySpace=None):
        """
            This method finds an empty space in a board. Empty spaces are represented 
            with 0.

            Params
            ------
            - board: <SudokuBoard> object. this function will use 'board' attribute of the object 
                     given to search for the empty space. If None, the method will use the 
                     'self.board' board.

            -emptySpace: <int> object. If is given, then we will search for the n-th empty space
                         (n = emptySpace). If not given, then the method will return the first
                         empty space that it finds.

            Returns
            -------
            - If empty space was found, then a <tuple> object is returned which contains the 
              empty space coordinates: (row, col)
            - If no empty space was found, then returns None.
            
        """

        # board selection
        if board:
            b = board.board
        else:
            b = self.board
        
        # Aux. variable to search the n-th empty space in case it is required
        k = 0

        # Nested loops to iterate the boaord
        for row in range(len(b)):
            for col in range(len(b)):
                # If an empty space was found, decide if a return is needed
                if b[row][col] == 0:
                    if not emptySpace:
                        return (row, col)
                    else:
                        if k == emptySpace:
                            return (row, col)
                        k += 1
        
        return None

    def __checkRules(self, num, space):
        """
            This method checks if a number can be placed in certain space following the
            Sudoku Rules.

            Params
            ------
            num: <int> object from 1 to 9
            space: <tuple> object with (row, col) coordinates of the space

            Return
            ------
            - False if the number cannot be placed in the space according to
              Sudoku rules or if the space already contains a number
            - True if the number can be placed in the space.
        """
               
        # Checking if the number is already in the same row as the space
        for col in self.board[space[0]]:
            if col == num:
                return False

        # Checking if the number is already in the same column as the space
        for row in range(len(self.board)):
            if self.board[row][space[1]] == num:
                return False
        
        # Checking if the number is already in the internal square which
        # the space belongs
        internalSquareRow = space[0] // 3
        internalSquareCol = space[1] // 3 

        for i in range(3):
            for j in range(3):
                if self.board[i + (internalSquareRow * 3)][j + (internalSquareCol * 3)] == num:
                    return False
        
        # If the number can be placed in the space, according to Sudoku rules, then
        # return True.
        return True
    
    def solve(self, initialCell=None):
        """
            This method implements a recursive BackTracking algorithm to solve
            the Sudoku Board.

            Params
            ------
            - initialCell: None by default. It expects a <tuple> object with (row, col) coordinates
                           of an empty space. If this parameter is given, then the board will begin
                           to be solved from the corresponding initial cell. If this parameter is
                           not given, the board will begin to be solved from the firs empty space
                           the algorithm find.

            Returns
            -------
            - True if the board could be solved.
            - False is the puzzle couldn't be solved.
        """

        # To store the available space.
        availableSpace = None

        # If initialCell was given, availableSpace = initialCell. Else, the algorithm will
        # search an available space
        if not initialCell:
            # Checking if there are empty spaces. If no empty spaces remains, then return True beacuse
            # it was possible to solve the puzzle.
            availableSpace = self.__findEmptySpace()
            if not availableSpace:
                return True
        else:
            availableSpace = initialCell

        # If there are an empty space, then try to fit the space with all valid numbers (1-9) 
        # according to Sudoku rules and try to solve it from this state. If there are no solution 
        # from the current configuration, then the next valid number is tried in the current space.

        # List of valid numbers (1-9)
        validNumbers = list(range(1, 10))

        # Trying all possible numbers (choosing them randomly) in the current availableSpace
        while validNumbers:
            n = validNumbers.pop(random.randrange(len(validNumbers)))
            # Checking if is possible to set the number according to Sudoku rules. If we can't, 
            # then continue to the next iteration to try with the next number
            if self.__checkRules(n, availableSpace):
                # If we don't broke any sudoku rule setting 'n' in the availableSpace, then put the
                # number 
                self.board[availableSpace[0]][availableSpace[1]] = n

                # try to RECURSIVELY SOLVE the puzzle with the current state (with the 'n' number 
                # added in the availableScpace)
                if self.solve():
                    # If the puzzle could be solved, then return True
                    return True
                
                # if the puzzle couldn't be solved with the 'n' number added in the available space, 
                # then reset the availableSpace with 0 and continue to the next iteration; that is,
                # try the next number that can fit in the availableSpace keeping the board solvable
                self.board[availableSpace[0]][availableSpace[1]] = 0
        
        # If any number (1-9) can fit in the availableSpace, then return False because the
        # puzzle can not be solved from the current configuration
        return False

    def __generateFullBoard(self):
        """
            This method generates a new random and filled Sudoku board following the rules of the
            game.
        """
        # Populate the board with 0's|
        self.__resetBoard()

        # Populate the three diagonal boxes

        # As we know, every diagonal box is independent from the other two diagonal boxes,
        # so we can fill each of them independently only checking that each number (1-9) only 
        # exists once in each box.

        # For loop to iterate the three boxes
        for i in range(1,4):
            # As the boxes are diagonal, then (x,y) coordinates for their first and last cells will 
            # be equals.

            # Getting the begin coordinate of the box
            boxBegin = 3*(i-1)
            # Getting the end coordinate of the box
            boxEnd = 3*i
            # List with the valid numbers
            validNumbers = list(range(1, 10))
            # Iterate the box
            for row in range(boxBegin, boxEnd):
                for col in range(boxBegin, boxEnd):
                    # Assign a random valid number. To assure that every single number will exist
                    # only once in the box, it is removed when it is selected. 
                    self.board[row][col] = validNumbers.pop(random.randrange(len(validNumbers)))
        
        # Populate the rest of the cells solving the board
        self.solve()

    def __findNumberOfSolutions(self):
        """
            This method finds the number of solutions a non-completely filled board has.

            Returns
            -------
            - List of <str> objects with length 81. Each of them represents a different 
              solution.
        """

        # Integer to store the number of empty spaces
        numberOfEmptySpaces = 0
        # List to store the solutions.
        list_of_solutions = []

        # Nested for loops to count the number of empty spaces in the board
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    numberOfEmptySpaces += 1

        # For loop to begin to solve the board from every single empty space found
        for i in range(numberOfEmptySpaces):
            # Copy of the original board
            board_copy = copy.deepcopy(self)
            # Getting the current empty space
            row, col = self.__findEmptySpace(board=board_copy, emptySpace=i)
            # Solving the puzzle from the current empty space
            board_copy.solve(initialCell=(row, col))
            # Storing the current solution
            list_of_solutions.append(board_copy.boardAsString())
        
        # Return the number of unique solutions
        return list(set(list_of_solutions))

    
    def generateGameBoard(self, emptySpaces=0):
        """
            This method generates a game board; that is, a partially filled Sudoku board
            with just one solution.

            Params
            ------
            - emptySpaces: <int> which represents the number of empty spaces the board will have.
                           By default, 0.
            
            Returns
            -------
            - Two <SudokuBoard> objects. The first one containing the 
              solved board; the last one is the partially filled board.
        """
        # Generating the full board and storing it
        self.__generateFullBoard()
        fullBoard = copy.deepcopy(self)

        # We erase "emptySpaces" number of cells randomly always checking that 
        # the number of solutions is 1.
        emptiedCells = 0
        while emptiedCells < emptySpaces:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            if self.board[row][col] != 0:
                n = self.board[row][col]
                self.board[row][col] = 0

                if len(self.__findNumberOfSolutions()) != 1:
                    self.board[row][col] = n
                    continue
                
                emptiedCells += 1
        
        # returns the solved board and the unsolved board
        if emptySpaces > 0:
            return fullBoard, self
        
        return self, None