import numpy as np

#Print a go board
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.board = np.array(self.board)
    def show_board(self):
        print(self.board)

my_go_match = Board(4)
my_go_match.show_board()