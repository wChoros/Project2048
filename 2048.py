import pygame
import numpy as np
import random
import msvcrt as m

icon = pygame.image.load('icona.png')
pygame.display.set_icon(icon)

def winlose(T):
    for i in range(0, 3):
        for j in range(0, 3):
            if T[i][j] == 2048:
                return False

    D = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

    Copy(D, T)
    D[3][0] = T[3][0]
    D[3][1] = T[3][1]
    D[3][2] = T[3][2]
    D[3][3] = T[3][3]

    D[0][3] = T[0][3]
    D[1][3] = T[1][3]
    D[2][3] = T[2][3]

    Left(D)
    if Comp(D, T):
        return True

    Right(D)
    if Comp(D, T):
        return True

    Up(D)
    if Comp(D, T):
        return True
    Down(D)

    if Comp(D, T):
        return True

    return False


def Comp(A, T):
    for i in range(0, 4):
        for j in range(0, 4):
            if A[i][j] != T[i][j]:
                return True
    return False


def Copy(A, T):
    for i in range(0, 4):
        for j in range(0, 4):
            A[i][j] = T[i][j]
    return A


def PrintT(T):
    for i in range(0, len(T)):
        a = ""
        for j in range(0, len(T[i])):
            a = a + " " + str(T[i][j])
        print(a)
    print("\n")


def RandSpawn(T):
    flag = True
    x = random.randint(1, 10)
    if (x > 2):
        x = 2
    else:
        x = 4

    while (flag == True):
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        if (T[a][b] == 0):
            flag = False
            T[a][b] = x

    return T


def Left(T):
    for i in range(0, len(T)):
        for l in range(4):
            for j in range(1, len(T[i])):
                if T[i][j - 1] == 0 and T[i][j] != 0:
                    T[i][j - 1] = T[i][j]
                    T[i][j] = 0
        for j in range(1, len(T[i])):
            if T[i][j] == T[i][j - 1]:
                T[i][j - 1] = T[i][j] * 2
                T[i][j] = 0
        for l in range(4):
            for j in range(1, len(T[i])):
                if T[i][j - 1] == 0 and T[i][j] != 0:
                    T[i][j - 1] = T[i][j]
                    T[i][j] = 0
    return T


def Right(T):
    for i in range(0, len(T)):
        for l in range(4):
            for j in range(2, -1, -1):
                if T[i][j + 1] == 0 and T[i][j] != 0:
                    T[i][j + 1] = T[i][j]
                    T[i][j] = 0
        for j in range(2, -1, -1):
            if T[i][j] == T[i][j + 1]:
                T[i][j + 1] = T[i][j] * 2
                T[i][j] = 0
        for l in range(4):
            for j in range(2, -1, -1):
                if T[i][j + 1] == 0 and T[i][j] != 0:
                    T[i][j + 1] = T[i][j]
                    T[i][j] = 0
    return T


def Down(T):
    for j in range(0, len(T)):
        for l in range(4):
            for i in range(2, -1, -1):
                if T[i + 1][j] == 0 and T[i][j] != 0:
                    T[i + 1][j] = T[i][j]
                    T[i][j] = 0
        for i in range(2, -1, -1):
            if T[i][j] == T[i + 1][j]:
                T[i + 1][j] = T[i][j] * 2
                T[i][j] = 0
        for l in range(4):
            for i in range(2, -1, -1):
                if T[i + 1][j] == 0 and T[i][j] != 0:
                    T[i + 1][j] = T[i][j]
                    T[i][j] = 0
    return T


def Up(T):
    for j in range(0, len(T)):
        for l in range(4):
            for i in range(1, 4):
                if T[i - 1][j] == 0 and T[i][j] != 0:
                    T[i - 1][j] = T[i][j]
                    T[i][j] = 0
        for i in range(1, 4):
            if T[i][j] == T[i - 1][j]:
                T[i - 1][j] = T[i][j] * 2
                T[i][j] = 0
        for l in range(4):
            for i in range(1, 4):
                if T[i - 1][j] == 0 and T[i][j] != 0:
                    T[i - 1][j] = T[i][j]
                    T[i][j] = 0

    return T



def tick(keys):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        Up(T)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        Left(T)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        Down(T)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        Right(T)

    if Comp(A, T):
        RandSpawn(T)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
N = 4
W = 480
H = W
SPACING = 18

T = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

A = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]


Copy(A, T)
RandSpawn(T)



pygame.init()
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("2048")

COLOR_MAP = {
    'back': (187, 173, 160),
    '0': (204, 192, 180),
    '2': (238, 228, 218),
    '4': (237, 224, 200),
    '8': (242, 177, 121),
    '16': (245, 149, 99),
    '32': (246, 124, 95),
    '64': (246, 94, 59),
    '128': (237, 207, 114),
    '256': (237, 204, 97),
    '512': (237, 200, 80),
    '1024': (237, 197, 63),
    '2048': (237, 194, 46)
}

def win():
    for i in range(0, 3):
        for j in range(0, 3):
            if T[i][j] == 2048:
                return True
def draw_window():
    window.fill((117, 117, 117))
    pygame.display.update()



def draw_game(myfont):
    window.fill(COLOR_MAP['back'])

    for i in range(0,4):
        for j in range(0,4):
            n = str(T[i][j])

            rect_x = j * W // N + SPACING
            rect_y = i * W // N + SPACING
            rect_w = W // N - 2 * SPACING
            rect_h = H // N - 2 * SPACING

            pygame.draw.rect(window,
                             COLOR_MAP[n],
                             pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                             border_radius=4)
            text_surface = myfont.render(str(T[i][j]), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(rect_x + rect_w/2,
                                                      rect_y + rect_h/2))
            window.blit(text_surface, text_rect)

def main():
    global T
    clock = 0
    score = 0
    run = True

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    Copy(A, T)

    draw_window()
    draw_game(myfont)
    pygame.display.flip()

    wasUp = True
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if winlose(T) == False:
            window.fill((117, 117, 117))
            if win():
                image1 = pygame.font.Font.render(pygame.font.SysFont("Futura", 80), f"You Won!", True,(255, 187, 0))
                image3 = pygame.image.load("obrazek.png")
                image2 = pygame.font.Font.render(pygame.font.SysFont("Futura", 30), f"Press any key to restart!", True,(0, 0, 0))
            if not win():
                image1 = pygame.font.Font.render(pygame.font.SysFont("Futura", 80), f"You Lost!", True,(255, 0, 0))
                image3 = pygame.image.load("obrazek1.png")
                image2 = pygame.font.Font.render(pygame.font.SysFont("Futura", 30), f"Press any key to restart!", True,(0, 0, 0))

            window.blit(image1, (100, 0))
            window.blit(image3, (0, 230))
            window.blit(image2, (0, 150))
            pygame.display.update()



            if True in keys and wasUp:
                T = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]



        if wasUp and True in keys:
            tick(pygame.key.get_pressed())
            draw_window()
            draw_game(myfont)
            pygame.display.flip()
            wasUp = False
            Copy(A, T)
        if not True in keys:
            wasUp = True





if __name__ == "__main__":
    main()