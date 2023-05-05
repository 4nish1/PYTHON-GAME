import pygame  # Import the Pygame library
import sys     # Import the sys library for system-specific parameters and functions

pygame.init()  # Initialize all imported Pygame modules

# Define constants for screen dimensions, paddle dimensions, ball dimensions, paddle speed, ball speed, and colors
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
BALL_SIZE = 20
BALL_SPEED = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create paddle and ball Rect objects
paddle1 = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set initial ball speed
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Initialize scores
score1 = 0
score2 = 0

# Set up the font for displaying scores
font = pygame.font.Font(None, 35)

# Main game loop
while True:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button, exit the game
            pygame.quit()
            sys.exit()

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()

    # Paddle 1 movement
    if keys[pygame.K_w] and paddle1.top > 0:  # Move paddle 1 up if the W key is pressed and paddle is not at the top edge
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:  # Move paddle 1 down if the S key is pressed and paddle is not at the bottom edge
        paddle1.y += PADDLE_SPEED

    # Paddle 2 movement
    if keys[pygame.K_UP] and paddle2.top > 0:  # Move paddle 2 up if the Up arrow key is pressed and paddle is not at the top edge
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:  # Move paddle 2 down if the Down arrow key is pressed and paddle is not at the bottom edge
        paddle2.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):  # If the ball collides with either paddle, reverse its horizontal speed
        ball_speed_x = -ball_speed_x

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:  # If the ball collides with the top or bottom edge, reverse its vertical speed
        ball_speed_y = -ball_speed_y

    # Ball collision with left and right
    if ball.left <= 0 or ball.right >= WIDTH:  # If the ball collides with the left or right edge, reset its position and reverse its horizontal speed
        if ball.left <= 0:
            score2 += 1
        else:
            score1 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x

    # Draw the paddles, ball, and dividing line
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    score_text = font.render(f"Player 1: {score1}  Player 2: {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.time.delay(16)