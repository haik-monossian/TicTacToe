cases={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}


def ask_player_cell(player_turn): # Ask at the player in which cell he want to play
    if player_turn == 1: # Player X
        cell = int(input("Player 1 turn (Enter a number 1 - 9) : "))
        while True : # Input security 
            if cell > 9 or cell < 1:
                cell = int(input("Retry, Player 1 turn (Enter a number 1 - 9 !!!) : "))
            elif cases[cell] != " ":
                cell = int(input("Cell taken !!, retry, Player 1 turn (Enter a number 1 - 9) : "))
            else:
                cases[cell]="X"
                break

    elif player_turn == 2: # Player O
        cell = int(input("Player 2 turn (Enter a number 1 - 9) : "))
        while True: # Input security
            if cases[cell] != " ":
                cell = int(input("Cell taken !!, retry, Player 2 turn (Enter a number 1 - 9) : "))
            else:
                cases[cell]="O"
                break


def change_player_turn(player_turn): # Change the player turn 
    if player_turn == 1 :
        return 2
    elif player_turn == 2 :
        return 1


def check_win_condition(game_is_running): # Check if there is a win combo or if it's a draw
    match cases:
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
            return False, "Player 2 Win"
        case {4:"O", 5:"O",6:"O"}:
            return False, "Player 2 Win"
        case {7:"O", 8:"O",9:"O"}:
            return False, "Player 2 Win"
        case {1:"O", 5:"O",9:"O"}:
            return False, "Player 2 Win"
        case {3:"O", 5:"O",7:"O"}:
            return False, "Player 2 Win"

    if all(value != " " for value in cases.values()):
        return False, "Draw"
    else :
        return game_is_running, None

def display_cells(): # Show the cells in the terminal
    print("")
    print(f" {cases[1]} | {cases[2]} | {cases[3]} ")
    print("-----------")
    print(f" {cases[4]} | {cases[5]} | {cases[6]} ")
    print("-----------")
    print(f" {cases[7]} | {cases[8]} | {cases[9]} ")
    print("")

def init_game(): # Game logic where we use all functions
    game_is_running = True
    player_turn = 1

    while game_is_running:
        ask_player_cell(player_turn)
        display_cells()
        game_is_running, message = check_win_condition(game_is_running)
        if message:
            print(message)
        player_turn = change_player_turn(player_turn)


#Start the game 
init_game()