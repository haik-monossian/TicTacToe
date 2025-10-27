Cases={1:"empty", 2:"empty", 3:"empty", 4:"empty", 5:"empty", 6:"empty", 7:"empty", 8:"empty", 9:"empty"};
PlayerTurn = 1;
GameIsRunning = True


def AskPlayerCell():
    if PlayerTurn == 1:
        cell = int(input("Player 1 turn (Enter a number 1 - 9) : "))
        while True:
            if Cases[cell] != "empty":
                cell = int(input("Cell taken !!, retry, Player 1 turn (Enter a number 1 - 9) : "))
            else:
                Cases[cell]="Cross"
                break

    elif PlayerTurn == 2:
        cell = int(input("Player 2 turn (Enter a number 1 - 9) : "))
        while True:
            if Cases[cell] != "empty":
                cell = int(input("Cell taken !!, retry, Player 2 turn (Enter a number 1 - 9) : "))
            else:
                Cases[cell]="Round"
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
        case {1:"Cross", 2:"Cross",3:"Cross"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {4:"Cross", 5:"Cross",6:"Cross"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {7:"Cross", 8:"Cross",9:"Cross"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {1:"Cross", 5:"Cross",9:"Cross"}:
            GameIsRunning = False
            return print("Player 1 Win")
        case {3:"Cross", 5:"Cross",7:"Cross"}:
            GameIsRunning = False
            return print("Player 1 Win")

        case {1:"Round", 2:"Round",3:"Round"}:
            GameIsRunning = False
            return print("Player 2 Win")
        case {4:"Round", 5:"Round",6:"Round"}:
            GameIsRunning = False
            return print("Player 2 Win")
        case {7:"Round", 8:"Round",9:"Round"}:
            GameIsRunning = False
            return print("Player 2 Win")
        case {1:"Round", 5:"Round",9:"Round"}:
            GameIsRunning = False
            return print("Player 2 Win")
        case {3:"Round", 5:"Round",7:"Round"}:
            GameIsRunning = False
            return print("Player 2 Win")

    if all(value != "empty" for value in Cases.values()):
        GameIsRunning = False
        return print("Draw")
    else:
        return 


def InitGame():
    while GameIsRunning:
        AskPlayerCell()
        print(Cases)
        CheckWinCondition()
        ChangePlayerTurn()


InitGame()