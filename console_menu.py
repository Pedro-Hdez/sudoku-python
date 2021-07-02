from sudokuBoard import SudokuBoard
import os

def printHeader():
    print("SUDOKU BOARD SOLVER AND GENERATOR")
    print("By Pedro Hernández\n")
    print("| -------------------------------------------------- |")
    print("| Github: https://github.com/Pedro-Hdez              |")
    print("| Portfolio (Spanish): https://pedro-hdez.github.io/ |")
    print("| -------------------------------------------------- |\n\n")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def showMenu():
    printHeader()

    print("Which action do you like to perform?")
    print("1: Solve a Sudoku")
    print("2: Generate new board")
    print("3: Read instructions")

    # Aux. variable to know if the usr input is valid
    valid_input = False
    # Variable to store user input
    usr_input = 0

    # Request an action until the user input is valid
    while not valid_input:
        usr_input = input("\nSelect an option:  ")
        # Checking if user input is a number
        try:
            usr_input = int(usr_input)
            # Checking if user input is 1 or 2
            if usr_input < 1 or usr_input > 3:
                raise Exception
            
            valid_input = True
        except:
            print("Error, invalid input. Please, select a valid option and try again.")
            continue
    
    clearConsole()

    return usr_input

def solveSudokuCase():
    print("SOLVE A SUDOKU\n\n")
    print("Please, write the 81 cell values below (Remember, empty cells are represented by 0)\n")

    valid_input = False
    while not valid_input:
        boardAsString = input(": ")
        charCounter = 0
        for c in boardAsString:
            try:
                int(c)
                charCounter += 1
            except:
                print("Error. Input must contain only digits. Please, try again.\n")    
                break
        
        if charCounter != 81:
            print("Error. Input length must have a length of 81 characters. Please, try again.\n")
            continue

        valid_input = True    

    b = SudokuBoard(board=boardAsString)
    print("\n\nORIGINAL BOARD")
    b.printBoard()
    print("\nSOLVED BOARD")
    b.solve()
    b.printBoard()
    input("\nPress a key to return to the main menu...")

def generateNewBoardCase():
    print("GENERATE NEW BOARD\n\n")
    valid_input = False
    emptySpaces = 0
    while not valid_input:
        emptySpaces = input("How many empty spaces do you want the board have? (0-50):  ")
        # Checking if user input is a number
        try:
            emptySpaces = int(emptySpaces)
            # Checking if user input is 1 or 2
            if emptySpaces < 0 or emptySpaces > 60:
                raise Exception
            
            valid_input = True
        except:
            print("Error, invalid input. Please, type a number in the range (0-60) and try again.")
            continue
    
    b = SudokuBoard()
    if emptySpaces > 0:
        filled, unfilled = b.generateGameBoard(emptySpaces=emptySpaces)
        print("\n\nNON-FILLED BOARD")
        unfilled.printBoard()
        print("\nFILLED BOARD")
        filled.printBoard()
    else:
        filled = b.generateGameBoard()
        print("\nFILLED BOARD")
        filled.printBoard()
    
    input("\nPress a key to return to the main menu...")

def readInstructionsCase():
    printHeader()

    print("INSTRUCTIONS\n")

    print("From main menu select an action to perform:")
    print("Press 1 to Solve a Sudoku")
    print("Press 2 to Generate new board")
    print("Press 3 to Read instructions\n\n")

    print("OPTION 1: SOLVE A SUDOKU\n")
    print("The program will request the board wrote as a 81 character string. Empty spaces are represented with the \'0\' character.")
    print("\nExample: Let the following board an unsolved sudoku:")
    
    b = SudokuBoard()
    b.generateGameBoard(emptySpaces=30)
    b.printBoard()

    print("\nIf you want to solve it, then you need to give the program the following string:\n")
    print(f": {b.boardAsString()}\n")
    print("Which contains the cells values row by row.\n\n")

    print("-----------------------------------------------\n\n")

    print("OPTION 2: GENERATE NEW BOARD\n")
    print("The program will request the number of empty spaces the new board will have (0-50).")
    print("If you want a random solved Sudoku board, then you need to request 0 empty spaces.")
    print("**NOTE** The more empty spaces you want, the slower the generation process will be.")


    input("\nPress a key to return to the main menu...")




if __name__ == "__main__":
    while True:
        clearConsole()
        usr_input = showMenu()

        if usr_input == 1:
            solveSudokuCase()
        elif usr_input == 2:
            generateNewBoardCase()
        elif usr_input == 3:
            readInstructionsCase()
            









    


    
    

