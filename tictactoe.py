import pygame

# --- Initialisation de Pygame ---
pygame.init()

# --- Configuration de la fenêtre ---
LARGEUR_ECRAN = 600
HAUTEUR_ECRAN = 600
DIMENSION_CASE = LARGEUR_ECRAN // 3 # Chaque case aura une dimension de 200x200 pour un 3x3
TITRE_FENETRE = "Tic-Tac-Toe Clicable"

screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption(TITRE_FENETRE)

# --- Couleurs ---
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS_CLAIR = (200, 200, 200)

# --- Initialisation du plateau (similaire à votre dictionnaire Cases) ---
# Nous allons stocker les objets Rect de Pygame pour chaque case,
# ce qui facilite la détection des clics.
board_rects = {} # Dictionnaire pour stocker les objets Rect et les associer aux numéros de case
# Les valeurs de Cases sont des espaces " " initialement
Cases = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

# --- Fonction pour dessiner le plateau ---
def draw_board():
    screen.fill(BLANC) # Fond blanc

    for i in range(3):
        for j in range(3):
            # Calcul des coordonnées x, y du coin supérieur gauche de la case
            x = j * DIMENSION_CASE
            y = i * DIMENSION_CASE
            
            # Calcul du numéro de la case (1 à 9)
            cell_number = i * 3 + j + 1

            # Création de l'objet Rect pour la case
            # Un Rect prend (x, y, largeur, hauteur)
            rect = pygame.Rect(x, y, DIMENSION_CASE, DIMENSION_CASE)
            board_rects[cell_number] = rect # Stocke le Rect dans notre dictionnaire

            # Dessiner le contour de la case
            pygame.draw.rect(screen, NOIR, rect, 3) # Le '3' est l'épaisseur du trait

            # Afficher le contenu de la case (X, O, ou vide)
            if Cases[cell_number] != " ":
                font = pygame.font.Font(None, 150) # Crée une police
                text_surface = font.render(Cases[cell_number], True, NOIR) # Rend le texte
                text_rect = text_surface.get_rect(center=rect.center) # Centre le texte dans la case
                screen.blit(text_surface, text_rect) # Affiche le texte


# --- Boucle de jeu principale ---
running = True
player_turn = "X" # On commence avec le joueur X

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- Détection d'un clic de souris ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Clic gauche de la souris
                mouse_x, mouse_y = event.pos # Coordonnées du clic

                # Parcourir nos rectangles de cases pour voir lequel a été cliqué
                for cell_number, rect in board_rects.items():
                    if rect.collidepoint(mouse_x, mouse_y): # Vérifie si le clic est dans ce rectangle
                        if Cases[cell_number] == " ": # Si la case est vide
                            Cases[cell_number] = player_turn # Place le symbole du joueur actuel
                            print(f"Case {cell_number} cliquée par {player_turn}")
                            
                            # Changer de joueur pour le prochain tour
                            if player_turn == "X":
                                player_turn = "O"
                            else:
                                player_turn = "X"
                            
                            # Ici, vous appelleriez vos fonctions CheckWinCondition()
                            # ou CheckGameStatus() pour voir si le jeu est terminé.
                            # Par exemple:
                            # status = CheckGameStatus(Cases, "X", "O")
                            # if status is not None:
                            #     print(f"Jeu terminé! Statut: {status}")
                            #     running = False # Arrête la boucle de jeu
                        else:
                            print(f"Case {cell_number} déjà prise.")
                        break # Un clic ne peut être que dans une seule case, donc on peut sortir de la boucle

    # --- Dessin du plateau et mise à jour de l'affichage ---
    draw_board() # Redessine tout le plateau à chaque frame
    pygame.display.flip()

# --- Quitter Pygame ---
pygame.quit()
print("Jeu fermé.")