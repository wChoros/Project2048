import pygame
pygame.init()  # inicacja biblioteki



x=20
y=15
player=pygame.rect.Rect(x,y,100,100) #kwadrat


window = pygame.display.set_mode((1000, 800))  # tworzenie okna o określonym rozmiarze
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.fill((255,105,180))
    pygame.draw.rect(window, (255,255,0), player) # rysowanie obiektu
    pygame.display.update()
