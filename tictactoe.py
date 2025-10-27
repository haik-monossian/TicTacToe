import random

Cases={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "};
PlayerTurn = 1;
GameIsRunning = True


def AskPlayerCell():
    if PlayerTurn == 1:
        cell = int(input("Player 1 turn (Enter a number 1 - 9) : "))
        while True :
            if cell > 9 or cell < 1:
                cell = int(input("Retry, Player 1 turn (Enter a number 1 - 9 !!!) : "))
            elif Cases[cell] != " ":
                cell = int(input("Cell taken !!, retry, Player 1 turn (Enter a number 1 - 9) : "))
            else:
                Cases[cell]="X"
                break

    elif PlayerTurn == 2:
        cell = random.randint(1,9) # Generate a random number
        while True :
            if cell > 9 or cell < 1:
                cell = random.randint(1,9)
            elif Cases[cell] != " ":
                cell = random.randint(1,9)
            else:
                print(f"IA took {cell}")
                Cases[cell]="O"
                break


def ChangePlayerTurn():
    global PlayerTurn # We initialize the value as global cause he gonna create a local value

    if PlayerTurn == 1 :
        PlayerTurn = 2
    elif PlayerTurn == 2 :
        PlayerTurn = 1
    else:
        return error


def CheckWinCondition():
    global GameIsRunning

    match Cases:
        case {1:"X", 2:"X",3:"X"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {4:"X", 5:"X",6:"X"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {7:"X", 8:"X",9:"X"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {1:"X", 5:"X",9:"X"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {3:"X", 5:"X",7:"X"}:
            GameIsRunning = False
            return print("Player 1 Win")

        case {1:"O", 2:"O",3:"O"}:
            GameIsRunning = False
            return print("IA Win")
        case {4:"O", 5:"O",6:"O"}:
            GameIsRunning = False
            return print("IA Win")
        case {7:"O", 8:"O",9:"O"}:
            GameIsRunning = False
            return print("IA Win")
        case {1:"O", 5:"O",9:"O"}:
            GameIsRunning = False
            return print("IA Win")
        case {3:"O", 5:"O",7:"O"}:
            GameIsRunning = False
            return print("IA Win")

    if all(value != " " for value in Cases.values()):
        GameIsRunning = False
        return print("Draw")
    else:
        return 

def DisplayCells():
    print("")
    print(f" {Cases[1]} | {Cases[2]} | {Cases[3]} ")
    print("-----------")
    print(f" {Cases[4]} | {Cases[5]} | {Cases[6]} ")
    print("-----------")
    print(f" {Cases[7]} | {Cases[8]} | {Cases[9]} ")
    print("")


def InitGame():
    while GameIsRunning:
        AskPlayerCell()
        DisplayCells()
        CheckWinCondition()
        ChangePlayerTurn()


InitGame()