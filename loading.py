import pygame

pygame.init()  # inicacja biblioteki

x = 20
y = 15
kierunek = '2'
player = pygame.rect.Rect(x, y, 100, 100)  # kwadrat

window = pygame.display.set_mode((800, 800))  # tworzenie okna o określonym rozmiarze
run = True

while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    speed = 4
    keys = pygame.key.get_pressed() #przechwytywanie klawiotury

    if (x>=800 and ): #strzalka w prawo nacisnieta
        x=x-speed
        y=
    if keys[pygame.K_LEFT]: #strzalka w prawo nacisnieta
        x=x-4
    if keys[pygame.K_DOWN]: #strzalka w prawo nacisnieta
        y=y+4
    if keys[pygame.K_UP]: #strzalka w prawo nacisnieta
        y=y-4

    player = pygame.rect.Rect(x,y,100,100) #update obiektu

    window.fill((255, 105, 180))
    pygame.draw.rect(window, (255, 255, 0), player)  # rysowanie obiektu
    pygame.display.update()
