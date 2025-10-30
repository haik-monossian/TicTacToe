import random
cases={1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "};

def ask_player_cell(player_turn, mod):
    if player_turn == 1:
        cell = int(input("Player 1 turn (Enter a number 1 - 9) : "))
        while True :
            if cell > 9 or cell < 1:
                cell = int(input("Retry, Player 1 turn (Enter a number 1 - 9 !!!) : "))
            elif cases[cell] != " ":
                cell = int(input("Cell taken !!, retry, Player 1 turn (Enter a number 1 - 9) : "))
            else:
                cases[cell]="X"
                break

    elif player_turn == 2 and mod == 1:
        cell = random.randint(1,9)
        while True :
            if cases[cell] != " ":
                cell = random.randint(1,9)
            else:
                cases[cell]="O"
                break

    elif player_turn == 2 and mod == 2:
        cell = get_best_move(cases)
        print(f"IA took {cell}")
        cases[cell]="O"

    return player_turn

def change_player_turn(player_turn):
    if player_turn == 1 :
        return 2
    elif player_turn == 2 :
        return 1


def minimax(board, depth, is_maximizing):
    result = evaluate_board(board)

    if result !=0:
        return result

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float ('-inf')
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float ('inf')
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float ('-inf')
    best_move = None

    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def get_available_moves(board):
    return [key for key, value in board.items() if value == " "]

def is_board_full(board):
    return all(value != " " for value in board.values())

def evaluate_board(board):
    # Vérifie toutes les combinaisons gagnantes
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            if board[combo[0]] == 'O':
                return 1  # IA gagne
            elif board[combo[0]] == 'X':
                return -1  # Joueur gagne
    
    return 0  # Match nul ou jeu en cours


def check_win_condition(game_is_running):
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
            return False, "IA Win"
        case {4:"O", 5:"O",6:"O"}:
            return False, "IA Win"
        case {7:"O", 8:"O",9:"O"}:
            return False, "IA Win"
        case {1:"O", 5:"O",9:"O"}:
            return False, "IA Win"
        case {3:"O", 5:"O",7:"O"}:
            return False, "IA Win"

    if all(value != " " for value in cases.values()):
        return False, "Draw"
    else:
        return game_is_running, None

def display_cells():
    print("")
    print(f" {cases[1]} | {cases[2]} | {cases[3]} ")
    print("-----------")
    print(f" {cases[4]} | {cases[5]} | {cases[6]} ")
    print("-----------")
    print(f" {cases[7]} | {cases[8]} | {cases[9]} ")
    print("")


def init_game():
    player_turn = 1
    game_is_running = True
    mod = 0
    while True:
        if mod not in [1,2]:
            mod = int(input("Enter 1 : Easy / 2 : Hard : "))
        else:
            if mod == 1:
                print("Easy mod")
                
            elif mod == 2:
                print("Hard mod")
            break

    
    while game_is_running:
        ask_player_cell(player_turn, mod)
        display_cells()
        game_is_running, message = check_win_condition(game_is_running)
        if message:
            print(message)
        player_turn = change_player_turn(player_turn)


init_game()