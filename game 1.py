import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

# Set up the board
board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 50)

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            # Update the board
            if board[row][col] == '':
                board[row][col] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

    # Draw the board
    screen.fill(white)
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, black)
                screen.blit(text, (col * 100 + 25, row * 100 + 25))
            elif board[row][col] == 'O':
                text = font.render('O', True, black)
                screen.blit(text, (col * 100 + 25, row * 100 + 25))
            pygame.draw.rect(screen, black, pygame.Rect(col * 100, row * 100, 100, 100), 1)

    # Check for a win
    for row in range(3):
        if board[row] == board[row][1] == board[row][2] != '':
            print(board[row] + ' wins!')
            sys.exit()
    for col in range(3):
        if board[col] == board[1][col] == board[2][col] != '':
            print(board[col] + ' wins!')
            sys.exit()
    if board == board[1][1] == board[2][2] != '':
        print(board + ' wins!')
        sys.exit()
    if board[2] == board[1][1] == board[2] != '':
        print(board[2] + ' wins!')
        sys.exit()

    # Check for a tie
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        print('Tie!')
        sys.exit()

    # Update the screen
    pygame.display.flip()