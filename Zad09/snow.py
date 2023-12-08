import pygame
import random


pygame.init()


screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snowflake")


white = (255, 255, 255)
black = (0, 0, 0)


snowflakes = []
snowflake_size = 20
snowflake_speed = 2


def create_snowflakes():
    x = random.randint(0 + snowflake_size, screen_width - snowflake_size)
    y = -snowflake_size
    snowflakes.append([x, y])


def draw_snowflakes():
    for flake in snowflakes:
        pygame.draw.circle(screen, white, (flake[0], flake[1]), snowflake_size)


running = True
clock = pygame.time.Clock()

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for flake in snowflakes:
                if flake[0] <= mouse_pos[0] <= flake[0] + snowflake_size and flake[1] <= mouse_pos[1] <= flake[1] + snowflake_size:
                    snowflakes.remove(flake)

    create_snowflakes()

    for flake in snowflakes:
        flake[1] += snowflake_speed

    
    draw_snowflakes()

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
