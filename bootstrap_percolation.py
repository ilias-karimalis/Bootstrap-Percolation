from decimal import *
from random import randint
import matplotlib.pyplot as plt

# Default height and width
H = height = 10
W = width  = 10

# Instantiates the empty board with initial infection points
def initialize_board(empty_board, p):
    for i in range(int(p*size)):
        # Currently have multiple initial inits could be placed on same spot
        # Class bday problem could be relevant here!!!
        empty_board[randint(0,height-1)][randint(0,width-1)] = 1

# Executes the percolation algorithm
def generate_board(initial_board, g):
    for i in range(g):
        new_board = [[0 for x in range(width)] for y in range(height)]
        for j in range(height):
            for k in range(width):
                col_m1 = 1 if initial_board[(j-1+H)%H][k] > 0 else 0
                col_p1 = 1 if initial_board[(j+1+H)%H][k] > 0 else 0
                row_m1 = 1 if initial_board[j][(k-1+W)%W] > 0 else 0
                row_p1 = 1 if initial_board[j][(k+1+W)%W] > 0 else 0
                s = col_m1 + col_p1 + row_m1 + row_p1
                if initial_board[j][k] == 0 and s >= 2:
                    new_board[j][k] = i + 1
                else:
                    new_board[j][k] = initial_board[j][k]
        # print_board(new_board)
        initial_board = new_board
    return new_board

# Prints the board state to the terminal
def print_board(board):
    print(*board, sep='\n')

# Plots the board state
def draw_board(board):
    plt.imshow(board)
    plt.show()

if __name__ == '__main__':

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

    # Initialize board dimensions
    while True:
        try:
            H = height = int(input('Set board height: '))
        except ValueError:
            print("Please enter an integer")
        else:
            break

    while True:
        try:
            W = width = int(input('Set board width: '))
        except ValueError:
            print("Please enter an integer")
        else:
            break

    size = height * width

    # Instantiate empty board
    board = [[0 for x in range(width)] for y in range(height)]

    # Initializes random initial infections
    initialize_board(board, p)

    # Itterate over g to generate final board
    board = generate_board(board, size)

    # Plots the final board
    draw_board(board)

