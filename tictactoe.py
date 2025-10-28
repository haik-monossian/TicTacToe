import pygame

pygame.init()

HEIGHT = 600
WIDTH = 600
DIMENSION_CASE = WIDTH // 3
TITTLE = "Tic-Tac-Toe"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITTLE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

board_rects = {} 
Cases = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

def DrawBoard():
    screen.fill(WHITE)

    for i in range(3):
        for j in range(3):
            x = j * DIMENSION_CASE
            y = i * DIMENSION_CASE
        
            cell_number = i * 3 + j + 1

            rect = pygame.Rect(x, y, DIMENSION_CASE, DIMENSION_CASE)
            board_rects[cell_number] = rect # Stocke le Rect dans notre dictionnaire

            # Draw case border
            pygame.draw.rect(screen, BLACK, rect, 3) # 3 = Thickness

            # Show (X, O, ou empty)
            if Cases[cell_number] != " ":
                font = pygame.font.Font(None, 150) # Create a font style
                text_surface = font.render(Cases[cell_number], True, BLACK) # Render the Text
                text_rect = text_surface.get_rect(center=rect.center) # Text center
                screen.blit(text_surface, text_rect) # Show text

def CheckWinCondition():
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



# --- Game ---

running = True
player_turn = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- Clic event ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos

                for cell_number, rect in board_rects.items():
                    if rect.collidepoint(mouse_x, mouse_y):
                        if Cases[cell_number] == " ": 
                            Cases[cell_number] = player_turn
                            print(f"Cell {cell_number} clicked by {player_turn}")
                            
                            # Change turn
                            if player_turn == "X":
                                player_turn = "O"
                            else:
                                player_turn = "X"
                            
                            result = CheckWinCondition()
                            if result:
                                if result =="Draw":
                                    print("Draw")
                                else:
                                    print(f"Player {result} won")
                                running = False

                        else:
                            print(f"Cell {cell_number} already taken.")
                        break

    DrawBoard()
    pygame.display.flip()

pygame.quit()
print("Jeu fermé.")