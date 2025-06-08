import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Change Sprite")

# Initial sprite setup
sprite_rect = pygame.Rect(150, 150, 100, 100)
sprite_color = (255, 0, 0)  # Start with red

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Change to a random color
                sprite_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, sprite_color, sprite_rect)
    pygame.display.flip()

pygame.quit()