import pygame

pygame.init()

window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    window.fill((50, 100, 150))

    pygame.display.update()

pygame.quit()