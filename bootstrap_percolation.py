from decimal import *
from random import randint

H = height = 25
W = width  = 25
size   = height * width

def initialize_board(empty_board, p):
    for i in range(int(p*size)):
        # Currently have multiple initial inits could be placed on same spot
        # Class bday problem could be relevant here!!!
        empty_board[randint(0,height-1)][randint(0,width-1)] = 1

def generate_board(initial_board, g):
    for i in range(g-1):
        # TODO
        for j in range(height):
            for k in range(width):
                col_m1 = 1 if initial_board[(j-1+H)%H][k] > 0 else 0
                col_p1 = 1 if initial_board[(j+1+H)%H][k] > 0 else 0
                row_m1 = 1 if initial_board[j][(k-1+W)%W] > 0 else 0
                row_p1 = 1 if initial_board[j][(k+1+W)%W] > 0 else 0
                s = col_m1 + col_p1 + row_m1 + row_p1
                if initial_board[j][k] == 0 and s >= 2:
                    initial_board[j][k] = i + 1

def print_board(board):
    print(*board, sep='\n')


if __name__ == '__main__':
    board = [[0 for x in range(width)] for y in range(height)]

    # Initialize the input for the p value"
    while True:
        try:
            p = Decimal(input('Set initial infection ratio: '))
            assert 0 <= p <= 1
        except InvalidOperation:
            print("Please enter a decimal between 0 and 1")
        except AssertionError:
            print("Please enter a decimal between 0 and 1")
        else:
            break

    # Initialize the input for the number of generations
    while True:
        try:
            g = int(input("Set the number of generations to itterate: "))
        except ValueError:
            print("Please enter an integer")
        else:
            break

    # Initializes random initial infections
    initialize_board(board, p)

    # Itterate over g to generate final board
    generate_board(board, g)

    print_board(board)
