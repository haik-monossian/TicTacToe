import random

Cases={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "};

def AskPlayerCell(player_turn):
    if player_turn == 1:
        cell = int(input("Player 1 turn (Enter a number 1 - 9) : "))
        while True :
            if cell > 9 or cell < 1:
                cell = int(input("Retry, Player 1 turn (Enter a number 1 - 9 !!!) : "))
            elif Cases[cell] != " ":
                cell = int(input("Cell taken !!, retry, Player 1 turn (Enter a number 1 - 9) : "))
            else:
                Cases[cell]="X"
                break

    elif player_turn == 2:
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

    return player_turn  # Retourne le tour (inchangé ici, mais pour cohérence)

def ChangePlayerTurn(player_turn):
    if player_turn == 1 :
        return 2
    elif player_turn == 2 :
        return 1
    # Plus de return error nécessaire

def CheckWinCondition(game_is_running):
    match Cases:
        case {1:"X", 2:"X",3:"X"}:
            return False, "Player 1 Win"
        case {4:"X", 5:"X",6:"X"}:
            return False, "Player 1 Win"
        case {7:"X", 8:"X",9:"X"}:
            return False, "Player 1 Win"
        case {1:"X", 5:"X",9:"X"}:
            return False, "Player 1 Win"
        case {3:"X", 5:"X",7:"X"}:
            return False, "Player 1 Win"

        case {1:"O", 2:"O",3:"O"}:
            return False, "IA Win"
        case {4:"O", 5:"O",6:"O"}:
            return False, "IA Win"
        case {7:"O", 8:"O",9:"O"}:
            return False, "IA Win"
        case {1:"O", 5:"O",9:"O"}:
            return False, "IA Win"
        case {3:"O", 5:"O",7:"O"}:
            return False, "IA Win"

    if all(value != " " for value in Cases.values()):
        return False, "Draw"
    else:
        return game_is_running, None  # Aucun changement

def DisplayCells():
    print("")
    print(f" {Cases[1]} | {Cases[2]} | {Cases[3]} ")
    print("-----------")
    print(f" {Cases[4]} | {Cases[5]} | {Cases[6]} ")
    print("-----------")
    print(f" {Cases[7]} | {Cases[8]} | {Cases[9]} ")
    print("")


def InitGame():
    player_turn = 1
    game_is_running = True
    
    while game_is_running:
        AskPlayerCell(player_turn)
        DisplayCells()
        game_is_running, message = CheckWinCondition(game_is_running)
        if message:
            print(message)
        player_turn = ChangePlayerTurn(player_turn)


InitGame()