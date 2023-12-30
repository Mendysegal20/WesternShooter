import pygame
from const import *
from game import Game

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

def get_row_col(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    run = True
    game = Game(screen)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_row_col(x, y)
                game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == '__main__':
    main()



