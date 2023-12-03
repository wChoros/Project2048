import pygame
import random as random


pygame.init()  # inicacja biblioteki

window = pygame.display.set_mode((1900, 1000))  # tworzenie okna o określonym rozmiarze
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
    pygame.display.update()
