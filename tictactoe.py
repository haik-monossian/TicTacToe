import pygame
import random
import sys

pygame.init()

# --- Constants ---
HEIGHT = 600
WIDTH = 600
DIMENSION_CASE = WIDTH // 3
TITLE = "Tic-Tac-Toe"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

BACKGROUND_COLOR = (25, 25, 50)
WHITE = (200, 200, 200)
WHITE1 = (255, 255, 255)
BLUE = (70, 70, 255)
RED = (255, 70, 70)

board_rects = {}
Cases = {i: " " for i in range(1, 10)}
game_message = None
game_mode = None

# --- Display functions ---
def DrawBoard(): # Draw cases and symbols
    screen.fill(BACKGROUND_COLOR)

    for i in range(3):
        for j in range(3):
            x = j * DIMENSION_CASE
            y = i * DIMENSION_CASE
            cell_number = i * 3 + j + 1

            rect = pygame.Rect(x, y, DIMENSION_CASE, DIMENSION_CASE)
            board_rects[cell_number] = rect

            pygame.draw.rect(screen, WHITE, rect, 3)

            if Cases[cell_number] != " ":
                font = pygame.font.Font(None, 150)
                color = BLUE if Cases[cell_number] == "X" else RED
                text_surface = font.render(Cases[cell_number], True, color)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)

    if game_message:
        font = pygame.font.Font(None, 60)
        text_surface = font.render(game_message, True, WHITE1, BACKGROUND_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)


def draw_text(text, size, color, x, y): # Draw the win text for each player 
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)
    return rect


# --- Game logic ---
def CheckWinCondition(): # Check if there is a Win or a Draw for each step 
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]

    for condition in win_conditions:
        values = [Cases[pos] for pos in condition]
        if values[0] != " " and all(val == values[0] for val in values):
            return values[0]
    if all(case != " " for case in Cases.values()):
        return "Draw"
    return None


# --- IA ---
def ia_easy_move(): # Easy IA random logic
    empty_cells = [i for i, v in Cases.items() if v == " "]
    return random.choice(empty_cells) if empty_cells else None


def evaluate_board(): # Judge : if O win return 1 if X win return -1
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for a, b, c in win_conditions:
        if Cases[a] == Cases[b] == Cases[c]:
            if Cases[a] == "O":
                return 1
            elif Cases[a] == "X":
                return -1
    return 0


def minimax(is_maximizing): # Predict all patterns with O and X to find the best score with the atm position
    score = evaluate_board()
    if score != 0:
        return score
    if all(v != " " for v in Cases.values()):
        return 0

    if is_maximizing: # Find the best O play
        best_score = -999
        for key in Cases:
            if Cases[key] == " ":
                Cases[key] = "O"
                current_score = minimax(False)
                Cases[key] = " "
                best_score = max(best_score, current_score)
        return best_score
    else: # Find the best X play
        best_score = 999
        for key in Cases:
            if Cases[key] == " ":
                Cases[key] = "X"
                current_score = minimax(True)
                Cases[key] = " "
                best_score = min(best_score, current_score)
        return best_score


def ia_hard_move(): # Find the best cell to play by using minimax()
    best_score = -999
    best_move = None
    for key in Cases:
        if Cases[key] == " ":
            Cases[key] = "O"
            score = minimax(False)
            Cases[key] = " "
            if score > best_score:
                best_score = score
                best_move = key
    return best_move


# --- Main menu ---
def main_menu(): # Show Game menu
    global game_mode
    menu_running = True
    while menu_running:
        screen.fill(BACKGROUND_COLOR)
        draw_text("TIC TAC TOE", 80, WHITE, WIDTH // 2, 150)

        # buttons logic 
        play_btn1 = draw_text("Player vs Player", 50, BLUE, WIDTH // 2, 300)
        play_btn2 = draw_text("Player vs IA (Easy)", 50, BLUE, WIDTH // 2, 380)
        play_btn3 = draw_text("Player vs IA (Hard)", 50, BLUE, WIDTH // 2, 460)
        quit_btn = draw_text("Quit", 50, RED, WIDTH // 2, 540)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn1.collidepoint(event.pos):
                    game_mode = "PVP"
                    menu_running = False
                    game_loop()
                elif play_btn2.collidepoint(event.pos):
                    game_mode = "EASY"
                    menu_running = False
                    game_loop()
                elif play_btn3.collidepoint(event.pos):
                    game_mode = "HARD"
                    menu_running = False
                    game_loop()
                elif quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


# --- Game loop ---
def game_loop(): # All the game logic when the game start 
    global Cases, game_message
    running = True
    player_turn = "X"
    game_message = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            # --- Player click event ---
            if event.type == pygame.MOUSEBUTTONDOWN and game_message is None:
                if event.button == 1 and (game_mode == "PVP" or player_turn == "X"):
                    mouse_x, mouse_y = event.pos
                    for cell_number, rect in board_rects.items():
                        if rect.collidepoint(mouse_x, mouse_y):
                            if Cases[cell_number] == " ":
                                Cases[cell_number] = player_turn
                                
                                DrawBoard()
                                pygame.display.flip()

                                result = CheckWinCondition()
                                if result:
                                    game_message = f"{'Draw' if result=='Draw' else f'Player {result} won !'}"
                                else:
                                    player_turn = "O" if player_turn == "X" else "X"

                            break

            # --- Restart after end ---
            elif event.type == pygame.MOUSEBUTTONDOWN and game_message is not None:
                Cases = {i: " " for i in range(1, 10)}
                player_turn = "X"
                game_message = None

        # --- IA ---
        if game_message is None and player_turn == "O" and game_mode in ["EASY", "HARD"]:
            pygame.time.delay(300)
            move = ia_easy_move() if game_mode == "EASY" else ia_hard_move()
            if move:
                Cases[move] = "O"
                result = CheckWinCondition()
                if result:
                    game_message = f"{'Draw' if result=='Draw' else f'Player {result} won !'}"
                else:
                    player_turn = "X"

        DrawBoard()
        pygame.display.flip()


# --- Start ---
main_menu()
pygame.quit()
print("Game closed")
