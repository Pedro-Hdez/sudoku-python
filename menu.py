from sudokuBoard import SudokuBoard
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def showMenu():
    # Header c:
    print("SUDOKU BOARD SOLVER AND GENERATOR")
    print("By Pedro Hernández\n\n")

    print("Which action do you like to perform?")
    print("1: Solve a Sudoku")
    print("2: Generate a non-filled board")
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

if __name__ == "__main__":
    while True:
        clearConsole()
        usr_input = showMenu()

        if usr_input == 1:
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
        
        elif usr_input == 2:
            print("GENERATE A NON-FILLED BOARD\n\n")

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
            b.generatePartiallyFilledBoard(emptySpaces=emptySpaces)
            print("\n\nNON-FILLED BOARD")
            b.printBoard()
            print("\nSOLVED BOARD")
            b.solve()
            b.printBoard()
            input("\nPress a key to return to the main menu...")









    


    
    

