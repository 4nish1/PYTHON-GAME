import pygame
import random

pygame.init()

# Set up the screen
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Set up the bird
bird_x = 50
bird_y = 200
bird_speed = 0

# Set up the pipes
pipe_x = screen_width
pipe_gap = 100
pipe_width = 52
pipe_height = 320
pipe_top_height = random.randint(100, 250)
pipe_bottom_height = screen_height - pipe_top_height - pipe_gap

# Set up the game loop
clock = pygame.time.Clock()
score = 0
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    # Update the bird
    bird_speed += 0.5
    bird_y += bird_speed

    # Update the pipes
    pipe_x -= 5
    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_top_height = random.randint(100, 250)
        pipe_bottom_height = screen_height - pipe_top_height - pipe_gap
        score += 1

    # Check for collisions
    if bird_y < 0 or bird_y > screen_height - 20:
        game_over = True
    if bird_x + 20 > pipe_x and bird_x < pipe_x + pipe_width:
        if bird_y < pipe_top_height or bird_y + 20 > pipe_top_height + pipe_gap:
            game_over = True

    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (bird_x, bird_y, 20, 20))
    pygame.draw.rect(screen, (0, 0, 255), (pipe_x, 0, pipe_width, pipe_top_height))
    pygame.draw.rect(screen, (0, 0, 255), (pipe_x, pipe_top_height + pipe_gap, pipe_width, pipe_bottom_height))
    pygame.display.set_caption("Flappy Bird - Score: " + str(score))
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()