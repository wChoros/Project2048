import pygame
pygame.init()  # inicacja biblioteki

window = pygame.display.set_mode((1000, 800))  # tworzenie okna o określonym rozmiarze
image = pygame.image.load("obrazek.png")





def main():
    run = True
pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    speed = 4
    keys = pygame.key.get_pressed() #przechwytywanie klawiotury

    if keys[pygame.K_RIGHT]: #strzalka w prawo nacisnieta
        x=x+4
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


